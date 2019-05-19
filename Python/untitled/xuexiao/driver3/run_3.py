#!/usr/bin/python
# -*- coding:utf-8 -*-
from xuexiao.repoet.baogao import Baogao
with open('ww.txt','r') as f:
    bb=f.readlines()
if 'all' in bb[0]:
    Baogao('*')


else:
    Baogao(bb)