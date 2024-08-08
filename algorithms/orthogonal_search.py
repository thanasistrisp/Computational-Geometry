import numpy as np
import matplotlib.pyplot as plt
from math import ceil, floor

np.random.seed(10)

class Node:
    def __init__(self, point=None):
        self.point = point
        self.left = None
        self.right = None

def build_kd_tree(p, depth):
    """
    @param p: list of points
    @param depth: depth of the tree
    return: root of a kd tree that contains p
    """
    if len(p) == 1:
        return Node(p[0])
    
    elif depth % 2 == 0:
        p = p[p[:,0].argsort()]
        median = ceil(len(p) / 2)
        p1 = p[:median]
        p2 = p[median:]
    else:
        p = p[p[:,1].argsort()[::-1]]
        median = floor(len(p) / 2)
        p1 = p[:median]
        p2 = p[median:]

    left = build_kd_tree(p1, depth+1)
    right = build_kd_tree(p2, depth+1)
    v = Node()
    v.left = left
    v.right = right
    return v

# define R region
class Rectangle:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1 # x1 is the lower left x-coordinate
        self.x2 = x2 # x2 is the upper right x-coordinate
        self.y1 = y1 # y1 is the lower left y-coordinate
        self.y2 = y2 # y2 is the upper right y-coordinate

def kd_tree_investigation(v, R, result):
    """
    @param v: a node
    @param R: rectangle
    return: all points in the subtree rooted at v that are inside R
    """
    left = v.left
    right = v.right
    if v.point is not None:
        if R.x1 <= v.point[0] <= R.x2 and R.y1 <= v.point[1] <= R.y2:
            result.append(v.point)
    else:
        if is_inside_full(left, R):
            result += reference_subtree(left)
        else:
            if intersect(left, R):
                kd_tree_investigation(left, R, result)
        if is_inside_full(right, R):
            result += reference_subtree(right)
        else:
            if intersect(right, R):
                kd_tree_investigation(right, R, result)
    return result
    
    
def is_inside_full(v, R):
    """
    @param v: a node
    @param R: rectangle
    return: True if all points in the subtree rooted at v are inside R
    """
    if v.point is None:
        return is_inside_full(v.left, R) and is_inside_full(v.right, R)
    else:
        if R.x1 < v.point[0] < R.x2 and R.y1 < v.point[1] < R.y2:
            return True
        else:
            return False
    
def intersect(v, R):
    """
    @param v: a node
    @param R: rectangle
    return: True if some any point in the subtree rooted at v is inside R
    """
    if v.point is None:
        return intersect(v.left, R) or intersect(v.right, R)
    else:
        if R.x1 <= v.point[0] <= R.x2 and R.y1 <= v.point[1] <= R.y2:
            return True
        else:
            return False

def reference_subtree(v):
    """
    @param v: a node
    return: all points in the subtree rooted at v
    """
    if v is None:
        return []
    return reference_subtree(v.left) + [v.point] + reference_subtree(v.right)

def rectangle_search(p, R):
    """
    @param p: list of points
    @param R: rectangle
    return: all points in p that are inside R
    """
    root = build_kd_tree(p, 0)
    result = []
    kd_tree_investigation(root, R, result)
    result = [x for x in result if x is not None]
    return result

if __name__ == "__main__":

    x, y = np.random.uniform(0, 20, 70), np.random.uniform(0, 20, 70)
    points = np.array(list(zip(x, y)))

    rectangle = Rectangle(3,12,2,18)
    final = rectangle_search(points, rectangle)
    print(final)

    plt.scatter(x, y)
    plt.plot([rectangle.x1, rectangle.x2], [rectangle.y1, rectangle.y1], color='y')
    plt.plot([rectangle.x1, rectangle.x2], [rectangle.y2, rectangle.y2], color='y')
    plt.plot([rectangle.x1, rectangle.x1], [rectangle.y1, rectangle.y2], color='y')
    plt.plot([rectangle.x2, rectangle.x2], [rectangle.y1, rectangle.y2], color='y')

    for point in final:
        plt.scatter(point[0], point[1], color='r')
    plt.show()
