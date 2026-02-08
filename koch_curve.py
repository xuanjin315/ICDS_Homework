#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:30:18 2024

@author: bing
"""

from math import sin, cos, pi
from matplotlib import pyplot as plt


def get_u_coordinates(s, t):
  
  u_x=(t[0]-s[0])*cos(pi/3)-(t[1]-s[1])*sin(pi/3)+s[0]
  u_y=(t[0]-s[0])*sin(pi/3)+(t[1]-s[1])*cos(pi/3)+s[1]
  u=(u_x,u_y)
  return u
    

    
    



def get_s_coordinates(p1, p2):
    '''it returns the coordinates (x, y)'''
   
    s_x=(2*p1[0]+p2[0])/3
    s_y=(2*p1[1]+p2[1])/3
    s=(s_x,s_y)
    return s
    


def get_t_coordinates(p1, p2):
    '''it returns the coordinates (x, y)'''
    
    t_x=(p1[0]+2*p2[0])/3
    t_y=(p1[1]+2*p2[1])/3
    t=(t_x,t_y)
    return t
    


def koch_curve(p1, p2, n, n_max):
    '''it returns a list of coordinates (x, y)'''
    output=[]
    if n==n_max:
        output=[p1,p2]
        return output
    s=get_s_coordinates(p1,p2)
    t=get_t_coordinates(p1,p2)
    u=get_u_coordinates(s,t)
 
    output=(koch_curve(p1,s,n+1,n_max)[:-1]+koch_curve(s,u,n+1,n_max)[:-1]+koch_curve(u,t,n+1,n_max)[:-1]+koch_curve(t,p2,n+1,n_max))

            
    # 易错：递归调用的时候在循环外+=1无用
    
            
      
        
    
    return output



if __name__ == "__main__":
    p1 = (0, 0)
    p2 = (100, 0)
    n_max = 3
    coordinates = koch_curve(p1, p2, 0, n_max)
    x = [c[0] for c in coordinates]
    y = [c[1] for c in coordinates]
    plt.axis('equal')
    plt.plot(x, y)
    plt.show()
    