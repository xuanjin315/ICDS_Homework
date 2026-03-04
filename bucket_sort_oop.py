#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:14:13 2019

@author: xg7
"""

class Bucket:
    
    def __init__(self, idx, low, high):
        self.numbers = []
        self.index=idx
        self.low_bound=low
        self.high_bound=high
        
        
    
    def absorb(self, number):
        if number>=self.low_bound and number<=self.high_bound:
            self.numbers.append(number)
            return True
    
    def sort(self):
        lst=self.numbers
        for i in range (1, len(lst)):
            v=lst[i]
            j=i-1
            while j>=0 and lst[j]>v:
                lst[j+1]=lst[j]
                j-=1
            lst[j+1]=v
        return lst

        

def bucket_sort(lst):
    buckets = []
    idx = 0
    for i in range(0, 100, 10):
        bucket = Bucket(idx, i, i+9)
        buckets.append(bucket)
    
    for number in lst:
        for b in buckets:
            if b.absorb(number):
                break
    
    result = []
    for b in buckets:
        result.extend(b.sort())
    return result        
    
        
if __name__ == "__main__": 
    ## main 
    import random        
    random.seed(0)
    
    listA = []
    for i in range(100):
        a = random.randint(0,99)
        listA.append(a)
    sorted_list = bucket_sort(listA) 
    print(sorted_list)
