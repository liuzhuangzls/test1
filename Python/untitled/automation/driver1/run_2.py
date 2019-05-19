#!/usr/bin/python
# -*- coding:utf-8 -*-
from interface_test.repoet.baogao import Baogao
with open('qwe.txt','r') as f:
    bb=f.readlines()
if 'all' in bb[0]:
    Baogao('*')
else:
    Baogao(bb)
