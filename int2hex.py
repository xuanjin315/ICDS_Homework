#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:09:16 2020

@author: xg7
"""

def int_to_hexa(int_code):
    hex_names = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    number = int(int_code)
    if number == 0:
        return "0"
    output = ""
    while number > 0:
        remainder = number % 16
        output += hex_names[remainder]
        number = number // 16
    return output[::-1]




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