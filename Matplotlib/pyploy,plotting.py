import matplotlib.pyplot as plt
import numpy as np

#pyplot

xpoints = np.array([0, 5])
ypoints = np.array([0, 210])

plt.plot(xpoints, ypoints)
plt.show()



#plotting

xpoints = np.array([1, 5])
ypoints = np.array([3, 9])

plt.plot(xpoints, ypoints)
plt.show()

#plotting without line--start-end points o means ring

xpoints = np.array([1, 5])
ypoints = np.array([3, 9])

plt.plot(xpoints, ypoints, 'o')
plt.show()


#multiple points

xpoints = np.array([1, 3, 6, 18])
ypoints = np.array([5, 10, 4, 20])

plt.plot(xpoints, ypoints)
plt.show()

#default Xpoints

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()