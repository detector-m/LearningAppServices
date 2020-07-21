#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :communication_model.py
@说明        :
@时间        :2020/07/21 09:13:26
@作者        :Riven
@版本        :1.0.0
'''

class File:
    def __init__(self, filename, content=None, content_type=None, path=None) -> None:
        self.filename = filename
        self.content = content
        self.content_type = content_type
        self.path = path