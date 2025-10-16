import matplotlib.pyplot as plt
import numpy as np

#linestyle

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

ypoints = np.array([3, 10, 4, 10])
plt.plot(ypoints, ls = '--')
plt.show()

#linecolor

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = 'b')
plt.show()

#line width

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '10.5')
plt.show()

#multiple lines

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()