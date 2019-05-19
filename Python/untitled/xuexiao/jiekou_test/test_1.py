#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from xuexiao.config.qingqiu import xuex
from xuexiao.data1.duqu import zxc
class asd(unittest.TestCase):
    aa=zxc().qq()
    bb=xuex().chaxun
    def test_1(self):
        cc=self.bb(self.aa[0][0])
        self.assertEqual(cc['code'],0)
    def test_2(self):
        for i in range(1,len(self.aa)):
            dd=self.bb(self.aa[i][0])
            self.assertNotEqual(dd['code'],0)
if __name__ == '__main__':
    unittest.main()