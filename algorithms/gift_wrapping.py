import numpy as np

def gift_wrapping(p):
    S = p.copy()
    r0 = min(S, key=lambda x: x[0])
    r = r0
    nodes = [r]

    while True:
        u = S[0]
        tempSet = S.copy()
        tempSet.remove(u)
        for t in tempSet:
            if CW(r,u,t):
                u = t
            elif is_collinear(r,u,t) and is_between(r,u,t):
                u = t

        if u == r0:
            return nodes
        else:
            r = u
            S.remove(r)
            nodes.append(r)

def CW(p1,p2,p3):
    matrix = [[1, p1[0], p1[1]], [1, p2[0], p2[1]], [1, p3[0], p3[1]]]
    det = np.linalg.det(matrix)
    return det < 0

def is_collinear(p1,p2,p3):
    matrix = [[1, p1[0], p1[1]], [1, p2[0], p2[1]], [1, p3[0], p3[1]]]
    det = np.linalg.det(matrix)
    return det == 0

def is_between(p1,p2,p3):
    return p1[0] <= p2[0] <= p3[0] or p3[0] <= p2[0] <= p1[0] or p1[1] <= p2[1] <= p3[1] or p3[1] <= p2[1] <= p1[1]
