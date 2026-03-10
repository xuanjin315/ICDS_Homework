#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:20:57 2021

@author: bing
"""


def permute(nums):
    to_be_processed=nums
    if len(to_be_processed)<2:
        output=[]
        output.append(to_be_processed)
        return output
    
    if len(to_be_processed)==2:
        output=[]
        output.append(to_be_processed)
        to_be_processed[0],to_be_processed[1]=to_be_processed[1],to_be_processed[0]
        output.append(to_be_processed)
        return output
    output_big=[]
    for i in range(len(to_be_processed)):
        chosen=to_be_processed[i]
        remain=to_be_processed[:i]+to_be_processed[i+1:]
        
        for p in permute(remain):
            output_small=[chosen]+p
            output_big.append(output_small)
    return output_big
            
            

    


# tests

if __name__ == "__main__":
    nums = [1, 2, 3]
    p1 = permute(nums)
    print("Permutation:", p1)
    
    nums = [1, 1, 2]
    p1 = permute(nums)
    print("Permutation:", p1)

    nums = ['a', 'b', 'c', 'd']
    p2 = permute(nums)
    print("Permutation:", p2)
