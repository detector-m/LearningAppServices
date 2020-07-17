#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :encryption_utils.py
@说明        :
@时间        :2020/07/14 10:18:01
@作者        :Riven
@版本        :1.0.0
'''

import base64
import hashlib

import sys
sys.path.append('..')
from Utils.apr1 import hash_apr1

def md5_apr1(salt, text):
    return hash_apr1(salt, text)

def sha1(text):
    result = hashlib.sha1(text.encode('utf-8'))
    return base64.b64encode(result.digest()).decode('utf-8')


# if __name__ == '__main__':
#     print(__file__)