#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :collection_utils.py
@说明        :
@时间        :2020/07/13 17:54:21
@作者        :Riven
@版本        :1.0.0
'''

def get_first_existing(dict, *keys, default=None):
    for key in keys:
        if key in dict:
            return dict[key]

    return default

