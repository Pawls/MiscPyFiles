""" Due end of class Thursday

BONUS EXAM 1

NAMES: 
    Paul Davis
    Gabby Lazo
    Tiffany Harry
    Daniel Gomez
    
Write pseudo code in your script, then list all solutions in Python

Section 3.1
    3-7 (1 point each)
    30-33 (3 points each)
    Selection Sort (3 points)
    
p.233 Shaker sort (5 points)
"""
from math import ceil, floor

"""
#3
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    sum = 0
    for i=1 to n
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
#4
Input: (L = a1<=a2<=...<=an: where each ai is an integer), X integer
Algorithm:
    index = set()
    for i=1 to n
        if L[i] == X
            index.add(i)
    return index
Output: Location of occurrences of X in L

"""

def number4(self, x):
    index = set()
    for i in range(0, len(self)):
        if self[i] == x:
            index.add(i)
    return index

"""
#5
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    max = 0
    min = 0
    for i=1 to n
        if max < i:
            max = i
        if min > i:
            min = i
    return max and min
Output: The maximum, and minimum element in L
"""

def number5(self):
    temp_max = self[0]
    temp_min = self[0]
    for i in range(0, len(self)):
        if temp_max < self[i]:
            temp_max = self[i]
        if temp_min > self[i]:
            temp_min = self[i]
    return print(f'The max element is {temp_max} and the min element is {temp_min}')

"""
#6
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    negatives = 0
    for i=1 to n
        if L[i] < 0:
            negatives += 1
    return negatives
Output: The total number of negative integers in the list
"""

def number6(self):
    negatives = 0
    for i in range(0, len(self)):
        if self[i] < 0:
            negatives += 1
    return negatives

"""
#7
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    k = 1
    for i=1 to n
        if L[i] is even:
            k = L[i]
    return k
Output: The location of the last even integer in the list
"""

def number7(self):
    lasteven = 0
    for i in range(0, len(self)):
        if self[i] % 2 == 0:
            lasteven = i
    return lasteven

"""
#8
Input: (L = a1<=a2<=...<=an: where each ai is an integer)
Algorithm:
    k = 0
    for i=1 to n
        if L[i] is even and greater than or equal to L[k]:
            k = i
    return k
Output: The location of the highest even integer in the list
"""

def number8(self):
    k = 0
    for i in range(0, len(self)):
        if self[i] % 2 == 0 and self[i] >= self[k]:
            k = i
    return k

"""
31. Devise an algorithm that finds the first term of a sequence
of integers that equals some previous term in the
sequence.

INPUT:  (L = a1,a2,...an: where each ai is an integer)
ALGORITHM:
    for i=1 to n
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
        
OUTPUT: First element that is less than preceding element
"""

def number33(self):
    for i in range(1, len(self)):
        if self[i] < self[i-1]:
            return self[i]
        