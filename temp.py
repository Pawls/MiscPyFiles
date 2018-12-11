import numpy as np

x = [1, 2, 3, 4]

y = [2, 3, 4, 5]

"""
INPUT. n-dimensional vectors x and y

ALGORITHM.
    product = x1*y1
    for i=2 to n
        product = product + xi*yi
        
OUTPUT. product
"""

def dot_product(x, y):
    product = x[0]*y[0]
    for i in range(1, len(x)):
        product += x[i]*y[i]
    return product

def product(x,y):
    return sum(x[i]*y[i] for i in range(len(x)))

A = [[1, 2, 3], [4, 5, 6], [4, 5, -1]]
B = [[4, 5, 0], [4, 5, 6], [3, 2, 4]]

def union(x,y):
    return x+y
"""
def vector_add(x,y):
    xy = [0]
    xy[0] = x[0] + y[0]
    for i in range(1, len(x)):
        xy[i] = x[i]+y[i]
    return xy"""

def vector_add(x,y):
    xy = []
    for i in range(len(x)):
        temp_row = []
        for j in range(len(y)):
            temp_row.append(x[i][j] + y[i][j])
        xy.append(temp_row)
    return print(xy)

    

print(dot_product(x,y))
