#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :utils_unittest.py
@说明        :单元测试
@时间        :2020/07/13 14:54:58
@作者        :Riven
@版本        :1.0.0
'''

# import os

# print()
# print(os.getcwd())

import unittest

import sys
sys.path.append('..')
from Utils import os_utils
from Utils import date_utils


class UtilsTest(unittest.TestCase):
    def setUp(self):
        os_utils.set_mac()

    def tearDown(self):
        pass

    def test_os(self):
        self.assertTrue(os_utils.is_mac(), 'Not mac')
        # self.assertTrue(os_utils.is_linux(), 'It is Mac')

    def test_date(self):
        print(date_utils.datetime_now())
        # print(date_utils.astimezone())
        print(date_utils.get_current_millis())
        # self.assertIsNotNone(date_utils.)

if __name__ == '__main__':
    unittest.main()