"""
Section 3.1 Algorithms
Definition. An algorithm is a finite sequence of precise instructions for 
performing a computation or solving a problem.

Problem 1. Given a list L of n numbers, find the maximum element of L.
pseudo code:
    input: L = l1, l2, ..., ln: list of n numbers
    algorithm

"""
from math import ceil, floor

def maximum(self):
    temp_max = self[0]
    for i in range(1, len(self)):
        if temp_max < self[i]:
            temp_max = self[i]
    return temp_max

"""
problem 2. Given a list L of n distinct numbers and a number x, find the 
location of x in L, or determine that x is not in L.


"""

def is_in(x, self):
    location = -1
    for i in range(len(self)):
        if self[i] == x:
            location = i
    if location == -1:
        return f'{x} is not in list {self}'
    else:
        return f'{x} is at index {location}'
    
"""
HOMEWORK
Problem 3. Given a list L of n distinct integers in increasing order and a 
integer x, find the location of x in L, or determine that x is not in L.

(using the binary search algorithm from the book)

homewok, section 3.1 translate all 7 sorting algorithms into python code
"""

"""
Problem 4. Given a list L of distinct integers, sort L in increasing 
order.

pseudo code:
    #bubble sort algorithm
    input: L = l1, ..., ln: lost of n distinct integers
    Algorithm:
        for i = 1 to n-1:
            for j = 1 to n - i
                if lj > lj+1
                    swap lj and lj+1
        
        
    OUTPUT: L in sorted increasing order
"""

def bubble_sort(self):
    for i in range(0,len(self)-1):
        print(self)
        for j in range(0,len(self)-i-1):
            if self[j] > self[j+1]:
                self[j], self[j+1] = self[j+1], self[j]
    return self

"""
Problem. Given a list of integers in non-decreasing order, write an algorithm
(with pseudocode) that returns a list elements in the list that repeat

Input: (L = a1<=a2<=...<=an: where each ai is an integer)

repeats = {}
for i=1 to n-1
    if i = n+1 and i is not in repeats
        repeats add i
return repeats

Output: List of elements in L that repeat
"""

def repeating_elements(self):
    L = set()
    for i in range(0, len(self)-1):
        if self[i] == self[i+1] and self[i] not in L:
            L.add(self[i])
    return L


""" Due end of class Thursday

BONUS EXAM 1

NAMES: 
    Paul Davis
    
Write pseudo code in your script, then list all solutions in Python

Section 3.1
    3-7 (1 point each)
    30-33 (3 points each)
    Selection Sort (3 points)
    
p.233 Shaker sort (5 points)
"""

"""
#3
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    sum = 0
    for i=0 to n
        sum += L[i]
    return sum
Output: sum of integers in list

"""

def number3(self):
    temp_sum = 0
    for i in range(0, len(self)):
        temp_sum += self[i]
    return temp_sum

"""
31. Devise an algorithm that finds the first term of a sequence
of integers that equals some previous term in the
sequence.

INPUT:  (L = a1,a2,...an: where each ai is an integer)
ALGORITHM:
    for i=0 to n
        for j=0 to i
            if L[i] == L[j]
                return L[i]
OUTPUT: First element that is duplicate with some previous element
"""
def number31(self):
    for i in range(0, len(self)):
        for j in range(0, i):
            if self[i] == self[j]:
                return self[i]

"""
32. Devise an algorithm that finds all terms of a finite sequence
of integers that are greater than the sum of all
previous terms of the sequence.

INPUT:  (L = a1,a2,...an: where each ai is an integer)
ALGORITHM:
    sum = 0
    temp = set
    for i=1 to n
        if L[i] > sum
            temp.add(L[i])
        sum += L[i]
    return temp
OUTPUT: A set containing all elements that are larger than the sum of previous
elements
"""

def number32(self):
    temp_sum = self[0]
    temp_set = set()
    for i in range(1, len(self)):
        if self[i] > temp_sum:
            temp_set.add(self[i])
        temp_sum += self[i]
    if temp_set != set():
        return temp_set
    else:
        return print("No elements meet conditions")
    
"""
33. Devise an algorithm that finds the first term of a sequence
of positive integers that is less than the immediately preceding
term of the sequence

INPUT:  (L = a1,a2,...an: where each ai is an integer)
ALGORITHM:
    for i=1 to n
        if self[i] < self[i-1]:
            return self[i]
        
OUTPUT: A set containing all elements that are larger than the sum of previous
elements
"""

def number33(self):
    for i in range(1, len(self)):
        if self[i] < self[i-1]:
            return self[i]
        