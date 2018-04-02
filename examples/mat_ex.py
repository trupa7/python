import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd
#for visual

# x=np.linspace(0,10,100)
# y=np.sin(x)
# plt.plot(x,y) # plot x,y
#
# plt.xlabel("time")
# plt.ylabel("compexity")
# plt.title("my chart")
# plt.show() #to show plot

A=pd.read_csv("data2.csv").as_matrix()

a=A[:,0]
b=A[:,1]
plt.scatter(a,b) #plot as point
plt.show()

