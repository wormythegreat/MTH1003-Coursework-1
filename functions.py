import numpy as np

def mydata(studentID):
    # Generate a series of 6 data points, dependent on the
    # input argument studentID

    # DO NOT MODIFY THIS CODE
    # otherwise your coursework functions might not
    # work correctly when tested

    # This code is deliberately obscure - you are not
    # expected to understand it or even look at it!

    assert studentID < 1e9, "studentID exceeds maximum allowed"

    studentID += int(1e8)
    tmp = str(studentID)

    T = []
    for k in tmp:
        T.append(float(k))
    T = np.array(T)
    xoff = sum(T)/17 % 2 - 1
    x = np.linspace(0, 5, 6)
    x += 0.01 * x * x + xoff
    yoff = 0.1 + 0.5 * sum(T**2)/13
    kperm = [7, 5, 8, 4, 6, 1]
    p = [2, 3, 5, 4, 6, 1] + T[7]
    y = abs(T[kperm] - yoff) * (-1)**p

    return x, y

def myID ():
    return 740043893

def cubicfit (x, y, xhat):
    def L1(x,y,value): # where x and y are the points, value is the x part of L(x)
        pass
    def L2(x,y,value): # where x and y are the points, value is the x part of L(x)
        pass
    def L3(x,y,value): # where x and y are the points, value is the x part of L(x)
        pass
    def L4(x,y,value): # where x and y are the points, value is the x part of L(x)
        pass
    pass