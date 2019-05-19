#!/usr/bin/python
# -*- coding:utf-8 -*-
from interface_test.repoet.baogao import Baogao
with open('a.txt','r') as f:
    bb=f.readlines()
    print(bb)

if 'all' in bb[0]:
    Baogao('*')
else:
    Baogao(bb)