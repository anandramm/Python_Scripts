# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 22:27:11 2022

@author: Anandram
"""

test=list(range(1,101))
def find_out(num:list):
    if len(num)==1:
        return num[0]
    else:
        u=[]
        for i,j in enumerate(num):
            if i%2==0:
                u.append(j)
            else:
                pass
        find_out(u)
m=find_out(test)
print(m)