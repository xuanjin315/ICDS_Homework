#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:06:22 2024

@author: bing
"""

def insertion_sort_with_gap(lst, g):
    for i in range(1,len(lst)):
        v=lst[i]
        j=i-g
        while j>=0 and lst[j]>v:
            lst[j+g]=lst[j]
            j=j-g
        lst[j+g]=v
    return lst
        

def shell_sort(lst):
    G = [5, 3, 1]
    output=lst
    for i in G:
        output=insertion_sort_with_gap(output,i)
    return output



if __name__ == "__main__":
    
    lst = [ 10, 9, 5, 6, 8, 3, 2, 1, 4, 7]
    shell_sort(lst)
    print(lst)
    
    lst = [ 0, 1, 2, 3]
    shell_sort(lst)
    print(lst)