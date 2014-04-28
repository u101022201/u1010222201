# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 23:34:45 2014

@author: 游筌翔
"""

import math
s = int(raw_input('ENTER THE VALUE OF N: '))
n = s + 1
def cat(n):
    if n == 0:
        return 1
    else:
        return (4*n - 2)/( n + 1 ) * cat(n-1)

def print_cat(n):
    c1, c2 =  1,  1
    while c1 <=  cat(n):
        print(c1)
        c1, c2 =  c2, (4*n - 2)/ ( n + 1 ) * c2

print print_cat(n)
