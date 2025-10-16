import matplotlib.pyplot as plt
import numpy as np

#HISTOGRAMS

x = np.random.normal(170, 10, 2)
print(x)

x = np.random.normal(170, 15, 100)
plt.hist(x)
plt.show()


#PIE CHARTS

y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()

#labels
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.show()

#setting a angle
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

#explodes
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0.1, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

#shadow
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()

#legend and title
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title="fruits")
plt.show() 