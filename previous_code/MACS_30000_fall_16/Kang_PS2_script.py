'''
------------------------------------------------------------------------
This is Bobae's PS2:
The current script contains the codes only for exercises 1 and 3.
Codes for exercise 2 are in separate files: ex2script.py and ex2module.py.
------------------------------------------------------------------------
'''
# import packages
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 1(a): Write a fuction firsthalf()
def firsthalf(string):
    outcome = string[0:len(string)//2]
    return(outcome)
print('1.(a). test: america becomes', firsthalf('america'))

# 1(b): Write a function backward()
def backward(string):
    outcome = string[::-1]
    return(outcome)
print('1.(b). test: america becomes', backward('america'))

# 1(c) Write a function pig_latin()
def pig_latin(string):
    vowels = 'aeiou'
    if string[0] in vowels:
        outcome = string + 'hey'
    else:
        index = 1
        if string[index] in vowels:
            index
        else: index += 1
        outcome = string[index:] + string[:index] + 'ay'
    return(outcome)

print('1.(c). test 1: america becomes', pig_latin('america'))
print('1.(c). test 2: france becomes', pig_latin('france'))
print('1.(c). test 3: germany becomes', pig_latin('germany'))
print('1.(c). test 4: christmas becomes', pig_latin('christmas'))

# 1(d) Write a function that returns the greatest product of four adjacent numbers in the same direction
grid = np.load('grid.npy') # read in the 20 by 20 grid
def maxProduct4(grid):
    rowProduct4 = grid[:, :grid.shape[1]-3] * grid[:, 1:grid.shape[1]-2] * grid[:, 2:grid.shape[1]-1] * grid[:, 3:grid.shape[1]]
    colProduct4 = grid[:grid.shape[0]-3, :] * grid[1:grid.shape[0]-2, :] * grid[2:grid.shape[0]-1, :] * grid[3:grid.shape[0], :]
    diaProduct4 = grid[:grid.shape[0]-3, :grid.shape[1]-3] * grid[1:grid.shape[0]-2, 1:grid.shape[1]-2] * grid[2:grid.shape[0]-1, 2:grid.shape[1]-1] * grid[3:grid.shape[0], 3:grid.shape[1]]
    offdiaProduct4 = grid[3:grid.shape[0], :grid.shape[1]-3] * grid[2:grid.shape[0]-1, 1:grid.shape[1]-2] * grid[1:grid.shape[0]-2, 2:grid.shape[1]-1] * grid[:grid.shape[0]-3, 3:grid.shape[1]]

    maxProduct4 = max(np.max(rowProduct4), np.max(colProduct4), np.max(diaProduct4), np.max(offdiaProduct4))
    return(maxProduct4)
print('1.(d). The greatest product of four consecutive numbers equals to', maxProduct4(grid))

# 3(a) Write a function ipmstack()
A = np.array([0,2,4,1,3,5]).reshape(2,3)
B = np.array([3,0,0,3,3,0,3,3,3,]).reshape(3,3)
C = np.array([-2, 0, 0, 0, -2, 0, 0, 0, -2]).reshape(3,3)

def ipmstack(A, B, C):
    d1 = np.hstack((np.zeros((3, 3)), A.T, np.identity(3)))
    d2 = np.hstack((A, np.zeros((2, 2)), np.zeros((2, 3))))
    d3 = np.hstack((B, np.zeros((3, 2)), C))
    D = np.vstack((d1, d2, d3))
    return(D)
D = ipmstack(A, B, C)
print('3.(a). the outcome of ipmstack() is:')
print(D)

# 3(b) popagesex2015
# i. read in and wrangle the popagesex2015 data
popagesex2015 = DataFrame(pd.read_csv('popagesex2015.csv',
                                    skiprows=[0, 1, 2, 3, 4, 106, 208, 310],
                                    names = ['gender', 'age', 'pop10', 'pop11', 'pop12', 'pop13', 'pop14', 'pop15'],
                                    converters = {0: lambda x: {'0':'both', '1':'male', '2':'female'}[x]},
                                    index_col = [0, 1]))

# ii. the percent of the total population in a given year by gender
df2 = popagesex2015.drop('both', level=0).groupby(level = 0).sum().apply(lambda x: x/x.sum()*100)
print('3.(b).ii. the percent of the total population in a given year by gender:')
print(df2)

# iii. the average percent of the total population by age
df3 = popagesex2015.groupby(level=0).get_group('both').apply(lambda x: 100*x/(x.sum())).mean(axis=1)
print('3.(b).iii. the average percent of the total population by age:')
print(df3)
