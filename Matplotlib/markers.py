import matplotlib.pyplot as plt
import numpy as np

#markers

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()

#format strings

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r')# green og,yellow oy..etc
plt.show()

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o--')
plt.show()

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o-.')
plt.show()

#marker size

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 15)
plt.show()


#marker color
#edge
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#face
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 10, mec = 'y', mfc = 'y')
plt.show()