
name = "Magdalena Maria Ponikowska"
surname1 = name.split(" ")[0]
print(surname1)
sentence = "{} bought 4 kilos apples. {} likes apples."
sentence.format(surname, name)

#if we want one optional argument)
def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z
print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

import numpy as np
mylist = [1, 2, 3]
x = np.array(mylist)
print(x)

n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
print(n)

m = n.reshape(3,5) # reshape array to be 3x5
print(m)

k = n.resize(3,3)

#when you want an array filled with one given number
np.zeros((3,2)) # follow the same pattern e.g. np.ones(),  inside the bracket we set size(shape) of the array

np.eye(3) # ones on the diagonal and zeros elsewhere

np.diag() #extracts diagonal from the array

np.array([1, 2, 3] * 3)
array([1, 2, 3, 1, 2, 3, 1, 2, 3])
>>> np.repeat([1, 2, 3], 3)
array([1, 1, 1, 2, 2, 2, 3, 3, 3])

p = np.ones([2,3], int)
>>> print(p)
array([[1, 1, 1],
       [1, 1, 1]])
>>> np.vstack([p, 2*p]) #vertical
array([[1, 1, 1],
       [1, 1, 1],
       [2, 2, 2],
       [2, 2, 2]])
>>> np.hstack([p, 2*p]) #horizontal
array([[1, 1, 1, 2, 2, 2],
       [1, 1, 1, 2, 2, 2]])
>> #concatenating arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.concatenate([a,b])

# vertically stack the arrays
 np.vstack([x, grid])
Out[48]: array([[1, 2, 3],
 [9, 8, 7],
 [6, 5, 4]])
In[49]: # horizontally stack the arrays
 y = np.array([[99],
 [99]])
 np.hstack([grid, y])
Out[49]: array([[ 9, 8, 7, 99],
 [ 6, 5, 4, 99]])
       
a.argmin()
a.argmax()
a.sum()
a.min()
a.max()
a.mean()
a.std()

#if we want copy an array
c = b.copy()
#change all objects into one element
r_copy[:] = 10 

test = np.random.randint(0, 10, (4,3))
test

+ np.add Addition (e.g., 1 + 1 = 2)
- np.subtract Subtraction (e.g., 3 - 2 = 1)
- np.negative Unary negation (e.g., -2)
* np.multiply Multiplication (e.g., 2 * 3 = 6)
/ np.divide Division (e.g., 3 / 2 = 1.5)
// np.floor_divide Floor division (e.g., 3 // 2 = 1)
** np.power Exponentiation (e.g., 2 ** 3 = 8)
% np.mod Modulus/remainder (e.g., 9 % 4 = 1)
np.abs() #zwraca wartość bezwzględną liczby

x = np.arange(1,6)
np.add.reduce(x) #output 15
np.add.accumulate()

Function Name NaN-safe Version Description
np.sum np.nansum #Compute sum of elements
np.prod np.nanprod #Compute product of elements
np.mean np.nanmean #Compute median of elements
np.std np.nanstd #Compute standard deviation
np.var np.nanvar #Compute variance
np.min np.nanmin #Find minimum value
np.max np.nanmax #Find maximum value
np.argmin np.nanargmin #Find index of minimum value
np.argmax np.nanargmax #Find index of maximum value
np.median np.nanmedian #Compute median of elements
np.percentile np.nanpercentile #Compute rank-based statistics of elements
np.any N/A #Evaluate whether any elements are true
np.all N/A #Evaluate whether all elements are true

A = np.array([2, 0, 1, 8]) #increase a dimension
A.shape() => (4, )
A[np.newaxis, :] => array([2, 0, 1, 8])
A[:, np.newaxis] => 
array([[2]
       [0]
       [1]
       [8]])

  
https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
https://www.analyticsvidhya.com/blog/2018/05/24-ultimate-data-science-projects-to-boost-your-knowledge-and-skills/
