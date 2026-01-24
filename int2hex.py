#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:09:16 2020

@author: xg7
"""

def int_to_hexa(int_code):
    ##modified the following to the tests
    hex_names=["0","1","2",'3','4','5','6','7','8','9','A','B','C','D','E','F']
    output=''
    a=17
    b=1
    number=int(int_code)
    # int_code/16=a.....b
    while a>16:
        a=number//16
        b=number%16
        number=a
        output=output+hex_names[b]
    if not a==0:
        output=output+hex_names[a]
    result=output[::-1]     
    return result




##---test of your code, don't change the followings---##
if __name__ == "__main__":
    int_code = 12
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)

    int_code = 16
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)

    int_code = 255
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)