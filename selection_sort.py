#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:15:18 2024

@author: bing
"""

class SelectionSorter:
    """
    A class that performs Selection Sort on a list of numbers.
    """
    def __init__(self, data):
       self.data=data
    

    def sort(self):
        """
        Sort the list in ascending order using the Selection Sort algorithm.
        """
        for i in range(len(self.data)):
            min_j=i
            memo=self.data[i]
            for j in range(i,len(self.data)):
                if self.data[j]<self.data[min_j]:
                    min_j=j
            self.data[i]=self.data[min_j]
            self.data[min_j]=memo
                    
                    

    def __str__(self):
        """
        Return a string representation of the current list.
        """
        # TODO: return the list as a string
        return str(self.data)


if __name__ == "__main__":
    
    sorter1 = SelectionSorter([10, 9, 5, 6, 8, 3, 2, 1, 4, 7])
    sorter1.sort()
    print(sorter1)
    
    sorter2 = SelectionSorter([0, 1, 2, 3])
    sorter2.sort()
    print(sorter2)