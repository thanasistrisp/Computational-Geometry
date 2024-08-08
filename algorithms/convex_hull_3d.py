import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

np.random.seed(0)

p = np.random.rand(80,3)


def plot_points_3d(p):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(p[:,0], p[:,1], p[:,2])
    plt.show()

def plot_hull_3d(p, hull):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(p[:,0], p[:,1], p[:,2])
    for simplex in hull.simplices:
        ax.plot(p[simplex, 0], p[simplex, 1], p[simplex, 2], 'k-')
    plt.show()


plot_points_3d(p)

hull = ConvexHull(p)

plot_hull_3d(p, hull)
