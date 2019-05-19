#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from interface_test.config.qingqiu import qwe
from interface_test.data.duqu import Shuju
class qwe(unittest.TestCase):
    denglu =qwe().denglu
    data=Shuju().shuju()
    def test_1(self):
        aa = self.denglu(int(self.data[0][0]), int(self.data[0][1]))
        self.assertEqual(aa['code'], 0)
        return aa

    def test_2(self):
        for i in range(1, len(self.data)):
            bb = self.denglu(int(self.data[i][0]), int(self.data[i][1]))
            self.assertNotEqual(bb['code'], 0)


if __name__ == '__main__':
    unittest.main()