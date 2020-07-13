#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :object_utils.py
@说明        :
@时间        :2020/07/13 14:16:28
@作者        :Riven
@版本        :1.0.0
'''

def update_dict(dict, extension_dic, *, override=False, ignored_keys=None):
    for key, value in extension_dic.items():
        if (not override) and (key in dict):
            continue
        
        if ignored_keys and (key in ignored_keys):
            continue

        dict[key] = value

def merge_dicts(*dicts, override=False, ignored_keys=None):
    result = {}

    for dict in dicts:
        update_dict(result, dict, override=override, ignored_keys=ignored_keys)

    return result
