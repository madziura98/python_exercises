
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
