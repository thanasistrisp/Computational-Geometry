from algorithms.graham_scan import graham_scan
import numpy as np

def divide_and_conquer(p):
    S = p.copy()
    S.sort(key=lambda x: x[0])

    if len(S) <= 5:
        L = graham_scan(S)
        L.reverse()
        return L
    
    A = S[:len(S)//2]
    B = S[len(S)//2:]

    LA = divide_and_conquer(A)
    LB = divide_and_conquer(B)

    return merge(LA, LB)

def merge(LA, LB):
    A, B = upper_bridge(LA, LB)
    C, D = lower_bridge(LA, LB)

    L = []
    i = LA.index(A)
    j = LB.index(D)
    while LA[i] != C:
        L.append(LA[i])
        i = (i+1)%len(LA)
    L.append(C)
    while LB[j] != B:
        L.append(LB[j])
        j = (j+1)%len(LB)
    L.append(B)
    return L
    

def upper_bridge(LA, LB):
    Ai = max(LA, key=lambda x: x[0])
    Bj = min(LB, key=lambda x: x[0])
    i = LA.index(Ai)
    j = LB.index(Bj)
    while True:
        i0 =i
        j0 = j
        AiA = CCW(LA[i], LA[(i+1)%len(LA)], LA[(i+2)%len(LA)])
        AiB = CCW(LA[i], LA[(i+1)%len(LA)], LB[j])
        if AiA * AiB < 0:
            i = (i+1)%len(LA)
        BjA = CCW(LB[j], LB[(j-1)%len(LB)], LA[i])
        BjB = CCW(LB[j], LB[(j-1)%len(LB)], LB[(j-2)%len(LB)])
        if BjA * BjB < 0:
            j = (j-1)%len(LB)
        if i == i0 and j == j0:
            return LA[i], LB[j]
        
def lower_bridge(LA, LB):
    Ai = max(LA, key=lambda x: x[0])
    Bj = min(LB, key=lambda x: x[0])
    i = LA.index(Ai)
    j = LB.index(Bj)
    while True:
        i0 =i
        j0 = j
        AiA = CCW(LA[i], LA[(i-1)%len(LA)], LA[(i-2)%len(LA)])
        AiB = CCW(LA[i], LA[(i-1)%len(LA)], LB[j])
        if AiA * AiB < 0:
            i = (i-1)%len(LA)
        BjA = CCW(LB[j], LB[(j+1)%len(LB)], LA[i])
        BjB = CCW(LB[j], LB[(j+1)%len(LB)], LB[(j+2)%len(LB)])
        if BjA * BjB < 0:
            j = (j+1)%len(LB)
        if i == i0 and j == j0:
            return LA[i], LB[j]
        

def CCW(p1, p2, p3):
    matrix = [[1, p1[0], p1[1]], [1, p2[0], p2[1]], [1, p3[0], p3[1]]]
    det = np.linalg.det(matrix)
    return det
