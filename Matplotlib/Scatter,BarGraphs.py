import matplotlib.pyplot as plt
import numpy as np

#plotting as dots
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()

#compare and coloring
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y,color='black')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y,color='yellow')
plt.show()

#coloring each dot
x = np.array([5,7,8,7,2,17,2,9])
y = np.array([86,103,87,94,78,77,85,86])
colors = np.array(["green","yellow","pink","purple","beige","brown","cyan","magenta"])
plt.scatter(x, y, c=colors)
plt.show()

# BARGRAPHS

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()

#horizontal
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x,y)
plt.show()

#bar color
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y,color="yellow")
plt.show()

#width
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y,width=0.2)
plt.show()

#height
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x,y,height=0.5)
plt.show()