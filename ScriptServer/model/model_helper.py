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

sys.path.append('.')
from config.constants import FILE_TYPE_DIR, FILE_TYPE_FILE

ENV_VAR_PREFIX = '$$'
SECURE_MASK = '*' * 6

LOGGER = logging.getLogger('script_server.model_helper')

if __name__ == '__main__':
    print(__file__)