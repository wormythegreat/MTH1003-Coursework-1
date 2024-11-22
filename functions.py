#This file contains the functions need to plot the data for Coursework 1

#import numpy required for mydata() function
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
    #This is my Student ID so should match: 740043893
    ID = 740043893
    return ID

def cubicfit (x, y, xhat):
    #Takes in x and y arrays of length 4 each and xhat which is the x coord of the point you want to find

    #First sets up some varibles names to make it easier to read and write formulas
    x1,x2,x3,x4 = x[0],x[1],x[2],x[3]
    y1,y2,y3,y4 = y[0],y[1],y[2],y[3]


    #These are each of the Lagrange polynomials
    #Each one is specific to its specified x coord
    #So L2() gives 1 at x2 and 0 at x1, x3 and x4
    def L1(xhat):
        return ((xhat-x2)*(xhat-x3)*(xhat-x4))/((x1-x2)*(x1-x3)*(x1-x4))
    def L2(xhat):
        return ((xhat-x1)*(xhat-x3)*(xhat-x4))/((x2-x1)*(x2-x3)*(x2-x4))
    def L3(xhat):
        return ((xhat-x1)*(xhat-x2)*(xhat-x4))/((x3-x1)*(x3-x2)*(x3-x4))
    def L4(xhat):
        return ((xhat-x1)*(xhat-x2)*(xhat-x3))/((x4-x1)*(x4-x2)*(x4-x3))
    
    #Finally returns the formula for the Lagrange polynomials
    yhat = (y1*L1(xhat)) + (y2*L2(xhat)) + (y3*L3(xhat)) + (y4*L4(xhat))
    return yhat

def findroot(xL, xR):
    #Takes in a starting guess for the left and right bracket
    #The y values of these x points will have to be off opposite signs

    #Importing the data to use
    datX,datY = mydata(myID())
    #This creates a short hand function to quickly find f(x) rather than having to write out cubicfit(datX[1:5],datY[1:5],x) every time
    def f(x):
        return cubicfit(datX[1:5],datY[1:5],x)
    
    #This is just the first instance of the error, later it is calculated off xN
    error = abs(f(xL))

    #This while loop states while the guess is further than (10)^-5 then it wil find a xN between xL and xR
    while error >= 10**(-5):
        
        #Uses the Regula Falsi formula to find xN
        xN = ( (xL*f(xR)) - (xR*f(xL))  )   /   (f(xR) - f(xL))

        #Now it retains which ever bracket has the same sign as f(xN)
        if f(xN)*f(xL) <= 0:
            xR = xN
        else:
            xL=xN

        #Calculates the error based off xN
        #(Side note - originally i had this based off xL but under a couple of very specific tests it would not work as xR would be exactly
        #  on the root but it would take python a very very long time to slowly get the left bracket close enough to be within the error)
        error = abs(f(xN))
    
    #Finally returns the value once the error is small enough and it breaks out of the loop
    return xL