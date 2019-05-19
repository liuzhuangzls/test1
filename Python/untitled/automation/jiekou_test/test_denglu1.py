#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from automation.config1.qingqiu_1 import asd
from automation.data.duqu_1 import zxc
class qwe(unittest.TestCase):
    denglu =asd().abc
    print(denglu)
    data=zxc().xx()
    print(data)
    def test_1(self):
        aa = self.denglu(self.data)
        self.assertEqual(aa['code'], 0)
        return aa

    #
    # def test_2(self):
    #     for i in range(1, len(self.data)):
    #         bb = self.denglu(int(self.data[i][0]), int(self.data[i][1]))
    #         self.assertNotEqual(bb['code'], 0)


