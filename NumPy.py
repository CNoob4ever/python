import numpy as np

a = np.array([1,2])
print(a)

def pySum():
    a = np.array([0,1,2,3,4])
    b = np.array([5,6,7,8,9])
    return a**3 + b**3

print(pySum())

def pySum2():
    a = [0,1,2,3,4]
    b = [5,6,7,8,9]
    c = []

    for i in range(len(a)):
        c.append(a[i]**3 + b[i]**3);

    return c

print(pySum2())

