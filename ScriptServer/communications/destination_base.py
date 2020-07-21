#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :destination_base.py
@说明        :
@时间        :2020/07/21 09:16:47
@作者        :Riven
@版本        :1.0.0
'''

import abc

class Destination(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def send(self, title, body, files=None):
        pass