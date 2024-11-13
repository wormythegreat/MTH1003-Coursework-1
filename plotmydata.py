import matplotlib.pyplot as plt
from functions import *

x,y = mydata(myID())
plt.plot(x,y,"X")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.title("Plot of Points")
plt.show()