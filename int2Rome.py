#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:50:19 2020

@author: xg7
"""

def convert_to_Roman_numeral(n):
    output=''
    symbles_lines=[('M',1000),("CM",900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX', 9),('V',5),('IV', 4),('I',1)]
    for symble,line in symbles_lines:
        while n>=line:
            symble_number=n//line
            output+=symble_number*symble
            n=n%line
    
    return output 
    
    
    

        
    
        
        
    


##test
if __name__ == "__main__":
    n = 1800
    print(convert_to_Roman_numeral(n))