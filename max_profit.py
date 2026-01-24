#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:08:56 2024

@author: bing
"""



def max_difference(prices):
    max_left = prices[0]
    min_right = prices[1]
    max_diff = max_left - min_right

    for i in range(1, len(prices)):
        diff = max_left - prices[i]
        if diff > max_diff:
            max_diff = diff
        if prices[i] < min_right:
            min_right = prices[i]
        if prices[i] > max_left:
            max_left = prices[i]

    return max_diff
            
    ##input your code here
    
    
  



        


if __name__ == "__main__":
    
    prices = [800, 300, 600, 200, 100]
    # print(max_profit(prices))
    print(max_profit(prices))

    prices = [800, 300, 200, 100, 0]
    # print(max_profit(prices))
    print(max_profit(prices))