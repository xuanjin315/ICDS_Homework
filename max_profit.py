#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:08:56 2024

@author: bing
"""



def max_profit(prices):
    min_price = prices[0]
    max_diff = prices[1] - prices[0]

    for i in range(1, len(prices)):
        diff = prices[i] - min_price
        if diff > max_diff:
            max_diff = diff
        if prices[i] < min_price:
            min_price = prices[i]

    return max_diff
            
    ##input your code here
    
    
  



        


if __name__ == "__main__":
    
    prices = [800, 300, 600, 200, 100]
    # print(max_profit(prices))
    print(max_profit(prices))

    prices = [800, 300, 200, 100, 0]
    # print(max_profit(prices))
    print(max_profit(prices))