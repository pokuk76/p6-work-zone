import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import CubicSpline

from tf_transformations import quaternion_from_matrix

T = np.load("transforms.npy")

N = np.shape(T)[-1]

s = np.arange(N)/N

pose = np.zeros([7, N])

for i in range(N):
    pose[:3, i] = T[:3, 3, i]
    pose[3:, i] = np.array(quaternion_from_matrix(T[:, :, i]))

np.save("poses.npy", pose)

plt.figure()

plt.plot(s, pose.T, lw = 2.5)

plt.grid()

plt.show()
