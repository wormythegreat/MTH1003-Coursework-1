import matplotlib.pyplot as plt
from functions import *

x,y = mydata(myID())

px = np.linspace(x[1],x[4],100)
py = []
index = 0
for count in px:
    py.append(cubicfit(x[1:5],y[1:5],px[index]))
    index = index + 1

rootX = findroot(x[2],x[3])
rootY = cubicfit(x[1:5],y[1:5],rootX)


plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.plot(px,py,label="Cubic Function")
plt.plot(x,y,"ro", label="Points")
plt.plot(rootX,rootY,"o",color="black",label="Root")

plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.legend()
plt.title("Plot of Points")
plt.savefig("./plot.png")