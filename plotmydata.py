import matplotlib.pyplot as plt
from functions import *

x,y = mydata(myID())
plt.plot(x,y,"rX")

px = np.linspace(x[1],x[4],100)
py = []
index = 0
for count in px:
    py.append(cubicfit(x[1:5],y[1:5],px[index]))
    index = index + 1
plt.plot(px,py)

plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.title("Plot of Points")
plt.savefig("./plot.png")