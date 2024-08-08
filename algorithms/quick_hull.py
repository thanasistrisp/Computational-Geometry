import numpy as np

def quick_hull(p):
    leftmost = min(p, key=lambda x: x[0])
    rightmost = max(p, key=lambda x: x[0])
    topmost = max(p, key=lambda x: x[1])
    bottommost = min(p, key=lambda x: x[1])

    if leftmost == rightmost or leftmost == topmost or leftmost == bottommost or \
    rightmost == topmost or rightmost == bottommost or topmost == bottommost:
        raise ValueError('Choose an other algorithm')
    

    setp = set()
    for point in p:
        if not is_inside_tetragon(point, leftmost, rightmost, topmost, bottommost):
            setp.add(point)

    # call the recursive quick hull algorithm for each side of the tetragon
    temp = find_points_on_right_side(leftmost, topmost, setp)
    final = rec_quick_hull(leftmost, topmost, temp)
    temp = find_points_on_right_side(topmost, rightmost, setp)
    final = final.union(rec_quick_hull(topmost, rightmost, temp))
    temp = find_points_on_right_side(rightmost, bottommost, setp)
    final = final.union(rec_quick_hull(rightmost, bottommost, temp))
    temp = find_points_on_right_side(bottommost, leftmost, setp)
    final = final.union(rec_quick_hull(bottommost, leftmost, temp))
    
    final = list(final)

    final = sort_points(final)

    return final

def sort_points(p): # return the points in clockwise order as list of tuples
    p = np.array(p)
    centroid = np.mean(p, axis=0)
    angles = np.arctan2(p[:,1]-centroid[1], p[:,0]-centroid[0])
    p = p[np.argsort(angles)]
    l = []
    for point in p:
        l.append(tuple(point))
    return l
    

def rec_quick_hull(A,B,S):
    if len(S) == 2:
        return S

    C = find_farthest_point(A,B,S)

    if C == None:
        return {A,B}

    M = find_points_on_right_side(A,C,S)

    N = find_points_on_right_side(C,B,S)

    return rec_quick_hull(A,C,M).union(rec_quick_hull(C,B,N))

def distance(A,B,C): # calculate the distance between the line AB and the point C
    return abs((B[0]-A[0])*(A[1]-C[1])-(A[0]-C[0])*(B[1]-A[1]))/np.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)

def find_farthest_point(A,B,S): # find the point C that is farthest from the line AB
    max_dist = 0
    for point in S:
        dist = distance(A,B,point)
        if dist > max_dist:
            max_dist = dist
            C = point

    if max_dist == 0:
        return None

    return C


def find_points_on_right_side(A,B,S): # find the set of points in S that are on the right side of the line AB
    setp = set()
    for point in S:
        if not is_right_turn(A,B,point):
            setp.add(point)

    return setp

            

def is_inside_tetragon(point, leftmost, rightmost, topmost, bottommost):
    if is_right_turn(leftmost, topmost, point) and is_right_turn(topmost, rightmost, point) \
    and is_right_turn(rightmost, bottommost, point) and is_right_turn(bottommost, leftmost, point):
        return True

def is_right_turn(p1, p2, p3):
    matrix = [[1, p1[0], p1[1]], [1, p2[0], p2[1]], [1, p3[0], p3[1]]]
    det = np.linalg.det(matrix)
    if det < 0:
        return True
    else:
        return False
