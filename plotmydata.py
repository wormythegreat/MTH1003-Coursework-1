#This file creates a plot of 6 points, a cubic function between 4 of them, and the root of that cubic

#import matplotlib for plotting
import matplotlib.pyplot as plt
#import all functions from the previous file
from functions import *


#Retrieves the data for the plot
x,y = mydata(myID())


#This next section creates 2 arrays of size 100 which contain the x and y coords respectively of points in the cubic
#First an array of 100 equally sized points between the 2nd and 5th data point
px = np.linspace(x[1],x[4],100) #numpy can be used here because it was imported when functions was imported
#Sets up the corrosponding y array which is empty to start
py = []
#Starts the index at 0
index = 0
#Loops through each of the values in px which is the x coords adds the matching y coord to the y array
for count in px:
    #This appends to the end of the y array and gets the y value from the cubic fit function and passes in the x coord
    py.append(cubicfit(x[1:5],y[1:5],px[index]))
    #Adds one to the index for each loop
    index = index + 1


#This section finds the x and y coord of the root of the cubic equation
#The x coord is found by using the findroot() function explained in functions.py
#The starting guess here is the 3rd and 4th point
rootX = findroot(x[2],x[3])
#The y coord can then be found by applying the cubic function at rootX
rootY = cubicfit(x[1:5],y[1:5],rootX)


#This section plots all of the points and lines onto the graph
#.axhline() plots a horizontal line at y=0 basically adding an x-axis
plt.axhline(0,0,1,color="grey")
#.axvline() plots a vertical line at x=0 basically adding a y-axis
plt.axvline(0,0,1,color="grey")
#This plots the array of x and y that were made using the cubic function
plt.plot(px,py,label="Cubic Function")
#This plots the original 6 points got from mydata()
#The reason this is plotted after the cubic funciton is so that the points appear
# on top of the line and can be seen more easily
plt.plot(x,y,"ro", label="Points")
#This plots a single point which is the root where the cubic graph crosses the x-axis
plt.plot(rootX,rootY,"o",color="black",label="Root")


#This final section adds labels and saves the graph
#These add lables to the x and y axis
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
#This adds the legend to the graph
plt.legend()
#Adds a title
plt.title("Plot of Points")
#Saves the graph to this directory with . being the current directory
plt.savefig("./yplot.png")