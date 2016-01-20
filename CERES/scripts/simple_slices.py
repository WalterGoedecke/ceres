# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:12:31 2015

@author: walter
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

#######################
# First flat subplots
# # # # # # # # # # # #
            
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
#plt.plot(t, s1)
fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax1.plot(t, s1)
plt.xlabel('time (s)')
plt.ylabel('sine')

s2 = np.cos(2*np.pi*t)
fig = plt.figure()
ax2 = fig.add_subplot(3, 1, 2)
ax2.plot(t, s2)
plt.xlabel('time (s)')
plt.ylabel('cosine')

s3 = -np.sin(2*np.pi*t)
fig = plt.figure()
ax2 = fig.add_subplot(3, 1, 3)
ax2.plot(t, s3)
plt.xlabel('time (s)')
plt.ylabel('-cosine')

#######################

#######################
# 3-D plot.
# # # # # # # # # # # #
            
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#X, Y, Z = [t, s1, 0]

x_pnts = np.arange(0, 2, .05)
y_pnts = np.arange(-1, 1.0, .05)
z_levels = np.arange(0, 1.1, .5)

# Create mesh at z-levels. 
#X, Y = np.meshgrid(X, Y)
X, Y = np.meshgrid(x_pnts, y_pnts)
for z in z_levels:
    #ax.plot_wireframe(X, Y, z, rstride=10, cstride=10)
#    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)
    ax.plot_wireframe(X, Y, z, rstride=10, cstride=10, cmap=cm.coolwarm, color='red',
                       linewidth=.01, linestyle='dashed', antialiased=False)
                       
                       
ax.plot_wireframe(t, s1, 0, rstride=10, cstride=10, linewidth=2)
ax.plot_wireframe(t, s2, 0.5, rstride=10, cstride=10, linewidth=2)
ax.plot_wireframe(t, s3, 1, rstride=10, cstride=10, linewidth=2)


ax.grid(True)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_zlabel('Slice')

#######################
