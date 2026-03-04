#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q6 Unified OOP Sorting (Inheritance · Polymorphism · Encapsulation)
Starter code — per the simplified requirements:
- Use ABC / @abstractmethod only (no getters/setters, no @property).
- sort() must return a NEW list (do not modify the original data).
- Insertion/Shell/Selection must NOT use sorted() / list.sort() in core logic.
- BucketSorter may use sorted() INSIDE each bucket only.
"""

from abc import ABC, abstractmethod
import random


# ------------------------------
# Base class (Abstract)
# ------------------------------
class Sorter(ABC):
    def __init__(self, name="Sorter"):
        self.name = name
        self._data = []   # protected attribute to hold input data

    @abstractmethod
    def sort(self):
        """Return a NEW sorted list based on self._data."""
        pass


# ------------------------------
# Insertion Sort
# ------------------------------
class InsertionSorter(Sorter):
    def __init__(self):
        super().__init__("InsertionSort")

    def sort(self):
        """
        TODO:
        - Make a copy of self._data: a = list(self._data)
        - Implement insertion sort on 'a' WITHOUT using sorted()/list.sort()
        - Return 'a' (a NEW list)
        """
        a=list(self._data)

        for i in range (1, len(a)):
            v=a[i]
            j=i-1
            while j>=0 and a[j]>v:
                a[j+1]=a[j]
                j-=1
            a[j+1]=v
        return a


# ------------------------------
# Shell Sort
# ------------------------------
class ShellSorter(Sorter):
    def __init__(self, gaps=None):
        super().__init__("ShellSort")
        # Default gaps if not provided
        self._gaps = [5, 3, 1] if gaps is None else gaps

    def sort(self):
        """
        TODO:
        - Copy self._data to 'a'
        - For each gap g in self._gaps, perform gapped insertion sort on 'a'
          (do NOT use sorted()/list.sort() here)
        - Return 'a'
        """
        a=list(self._data)
        def insertion_sort_with_gap(lst, gaps):
            for g in gaps:
                for i in range(1,len(lst)):
                    v=lst[i]
                    j=i-g
                    while j>=0 and lst[j]>v:
                        lst[j+g]=lst[j]
                        j=j-g
                    lst[j+g]=v
                return lst
        a=insertion_sort_with_gap(a,self._gaps)
        return a       
        


# ------------------------------
# Selection Sort
# ------------------------------
class SelectionSorter(Sorter):
    def __init__(self):
        super().__init__("SelectionSort")

    def sort(self):
        """
        TODO:
        - Copy self._data to 'a'
        - Implement selection sort on 'a' WITHOUT using sorted()/list.sort()
        - Return 'a'
        """
        a=list(self._data)
        for i in range(len(a)):
            min_j=i
            memo=a[i]
            for j in range(i,len(a)):
                if a[j]<a[min_j]:
                    min_j=j
            a[i]=a[min_j]
            a[min_j]=memo
        return a


# ------------------------------
# Bucket Sort (0–99, bucket size = 10)
# ------------------------------
class Bucket:
    def __init__(self, idx, low, high):
        """
        TODO:
        - Store idx, low, high
        - Prepare an empty list 'numbers' to hold absorbed elements
        """
        self.idx=idx
        self.low=low
        self.high=high
        self.numbers=[]

    def absorb(self, number):
        """
        TODO:
        - If low <= number <= high:
            append to self.numbers and return True
          else:
            return False
        """
        if self.low<=number and number<=self.high:
            self.numbers.append(number)
            return True
        else:
            return False

    def sort(self):
        """
        TODO:
        - Return a NEW sorted list of numbers in this bucket.
        - You MAY use built-in sorted() here.
        """
        self.numbers=sorted(self.numbers)
        return self.numbers


class BucketSorter(Sorter):
    def __init__(self):
        super().__init__("BucketSort")
        self._buckets = []

    def _build_buckets(self):
        """
        Build 10 buckets for ranges:
        [0–9], [10–19], …, [90–99]
        """
        # TODO: create Bucket(idx, low, high) and store in self._buckets
        for i in range(0,100,10):
            
            self._buckets.append(Bucket(i//10,i,i+10))

    def sort(self):
        """
        TODO:
        - Copy self._data to 'a'
        - Build buckets (call _build_buckets)
        - For each x in 'a', iterate buckets and call absorb(); break on success
        - Collect: create result list, extend with each bucket's sorted() result
        - Return the result list (NEW list)
        """
        a=list(self._data)
        self._build_buckets()
        for i in a:
            for b in self._buckets:
                if b.absorb(i):
                    break
        result=[]
        for b in self._buckets:
            result.extend(b.sort())
        return result


# ------------------------------
# Polymorphic runner
# ------------------------------
def run_all(sorters, lst):
    """
    Run all sorters on the same data and return results as a dict:
      { sorter.name: sorted_list }
    Steps:
      - For each sorter s:
          s._data = list(lst)   # make a copy so input is not modified
          out = s.sort()
          store into outputs[s.name] = out
    """
    # TODO: implement per description above
    dic={}
    for i in sorters:
        i._data=lst
        if i.name not in dic:
            dic[i.name]=[]
        dic[i.name]=i.sort()
    return dic
        


# ------------------------------
# Optional quick test (ungraded)
# ------------------------------
if __name__ == "__main__":
    random.seed(0)
    data = [random.randint(0, 99) for _ in range(20)]
    sorters = [InsertionSorter(), ShellSorter(), SelectionSorter(), BucketSorter()]
    results = run_all(sorters, data)

    # You can print results after you implement everything:
    for name, arr in results.items():
       print(name, arr)