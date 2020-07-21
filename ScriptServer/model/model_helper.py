#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :model_helper.py
@说明        :
@时间        :2020/07/21 17:14:42
@作者        :Riven
@版本        :1.0.0
'''

import logging, os, re

import sys
sys.path.append('..')
import Utils.env_utils as env_utils
from Utils.string_utils import is_blank
from Utils.utils_helper import is_empty

sys.path.append('.')
from config.constants import FILE_TYPE_DIR, FILE_TYPE_FILE

ENV_VAR_PREFIX = '$$'
SECURE_MASK = '*' * 6

LOGGER = logging.getLogger('script_server.model_helper')

def resolve_env_vars(value, *, full_match=False):
    if not isinstance(value, str) or is_empty(value):
        return value

    if full_match:
        if value.startswith(ENV_VAR_PREFIX):
            return env_utils.read_variable(value[2:])
        
        return value

    def resolve_var(match):
        var_match = match.group()
        var_name = var_match[2:]
        resolved = env_utils.read_variable(var_name, fail_on_missing=False)
        if resolved is not None:
            return resolved
        
        return var_match

    pattern = re.escape(ENV_VAR_PREFIX) + '\w+'

    return re.sub(pattern, resolve_var, value)

if __name__ == '__main__':
    print(__file__)