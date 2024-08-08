from algorithms.vis import plot_points, plot_KP2
import numpy as np

p = [(-10,5),(-2,-10),(1,7),(3,4),(5,6),(9,3),(11,8),(15,-11),(18,-3),(24,-8)] # example in slides


def graham_scan(p, visualize=False):
    p = sorted(p, key=lambda x: (x[0], x[1]))
    if visualize:
        print(p)

    L_upper = [p[0], p[1]]
    for i in range(2, len(p)):
        L_upper.append(p[i])
        if visualize:
            print("L_upper = ", end="")
            for j in range(len(L_upper)):
                print("p" + str(p.index(L_upper[j])+1), end="")
                if j != len(L_upper)-1:
                    print(", ", end="")
            print("")
        while len(L_upper) > 2 and not is_right_turn(L_upper[-3], L_upper[-2], L_upper[-1]):
            if visualize:
                print("Not right turn: p" + str(p.index(L_upper[-3])+1) + ", p" + str(p.index(L_upper[-2])+1) + ", p" + str(p.index(L_upper[-1])+1))
            del L_upper[-2]
        if visualize:
            plot_KP2(p, L_upper, "")

    L_lower = [p[-1], p[-2]]
    for i in range(len(p)-3, -1, -1):
        L_lower.append(p[i])
        while len(L_lower) > 2 and not is_right_turn(L_lower[-3], L_lower[-2], L_lower[-1]):
            if visualize:
                print("Not right turn: p" + str(p.index(L_lower[-3])+1) + ", p" + str(p.index(L_lower[-2])+1) + ", p" + str(p.index(L_lower[-1])+1))
            del L_lower[-2]
        if visualize:
            plot_KP2(p, L_lower, "")

    del L_lower[0]
    del L_lower[-1]

    L = L_upper + L_lower
    return L
    

def is_right_turn(p1, p2, p3):
    matrix = [[1, p1[0], p1[1]], [1, p2[0], p2[1]], [1, p3[0], p3[1]]]
    det = np.linalg.det(matrix)
    if det < 0:
        return True
    else:
        return False


def show_steps():
    plot_points(p)
    L = graham_scan(p, visualize=True)
    plot_KP2(p, L, "")

    print("L = {", end="")
    for i in range(len(L)):
        print("p" + str(p.index(L[i])+1), end="")
        if i != len(L)-1:
            print(", ", end="")
    print("}")
