#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :process_utils.py
@说明        :
@时间        :2020/07/16 16:20:09
@作者        :Riven
@版本        :1.0.0
'''

import logging
import os
import shlex
import subprocess

import sys
sys.path.append('..')
from Utils import os_utils, string_utils, file_utils

LOGGER = logging.getLogger('server.process_utils')

'''
Python函数独立星号（*）分隔的命名关键字参数
如果需要限制关键字参数的输入名字，就需要使用到命名关键字参数的形式，所谓命名关键字参数就是给关键字参数限定指定的名字，输入其他名字不能识别。命名关键字参数和位置参数之间使用独立的星号（*）分隔，星号后面为命名关键字参数，星号本身不是参数。凡是命名关键字参数，在调用时必须带参数名字进行调用，否则会报错。
命名关键字参数与关键字参数的区别有2点：
1、命名关键字参数是固定参数，不支持可变参数；
2、命名关键字参数在位置参数之后，二者之间用星号隔开。
'''

def invoke(command, work_dir='.', *, environment_variables=None, check_stderr=True):
    if isinstance(command, str):
        command = split_command(command, working_directory=work_dir)

    if environment_variables is not None:
        env = dict(os.environ, **environment_variables)
    else:
        env = None

    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=work_dir, env=env, universal_newlines=True)

    (output, error) = p.communicate()

    result_code = p.returncode
    if result_code != 0:
        raise ExecutionException(result_code, error, output)

    if error and check_stderr:
        LOGGER.warning("Error output wasn't empty, although the command finished with code 0!")

    return output

def split_command(script_command, working_directory=None):
    if ' ' in script_command:
        if _is_file_path(script_command, working_directory):
            args = [script_command]
        else:
            posix = not os_utils.is_win()
            args = shlex.split(script_command, posix=posix)

            if not posix:
                args = [string_utils.unwrap_quotes(arg) for arg in args]
    else:
        args = [script_command]
    
    script_path = file_utils.normalize_path(args[0], working_directory)
    if (not os.path.isabs(script_path)) or (os.path.exists(script_path)):
        script_path = args[0]
    
    script_args = args[1:]
    for i, body_arg in enumerate(script_args):
        expanded = os.path.expanduser(body_arg)
        if expanded != body_arg:
            script_args[i] = expanded
        
    return [script_path] + script_args

def _is_file_path(script_command_with_whitespaces, working_directory):
    if script_command_with_whitespaces.startswith('"') \
        or script_command_with_whitespaces.startswith("'"):
        return False
    
    file_exists = file_utils.exists(script_command_with_whitespaces, working_directory)
    if file_exists:
        LOGGER.warning('"%s" is a file with whitespaces'
                       ', please wrap it with quotes to avoid ambiguity',
                       script_command_with_whitespaces)

        return True
    
    return False

class ExecutionException(Exception):
    def __init__(self, exit_code, stderr, stdout):
        message = 'Execution failed. Code' + str(exit_code)
        if stderr:
            message += ': ' + stderr
        elif stdout:
            last_line_start = stdout.rfind('\n')
            message += ': ' + stdout[last_line_start:]

        super().__init__(message)

        self.stdout = stdout
        self.stderr = stderr
        self.exit_code = exit_code

if __name__ == '__main__':
    print(__file__)