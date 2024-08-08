from algorithms.graham_scan import graham_scan, show_steps
from algorithms.vis import plot_points, plot_KP2
from algorithms.gift_wrapping import gift_wrapping
from algorithms.divide_and_conquer import divide_and_conquer
from algorithms.quick_hull import quick_hull

import sys
import matplotlib.pyplot as plt

def print_points(L):
	for i in range(len(L)):
		print("p" + str(p.index(L[i])+1), end="")
		if i != len(L)-1:
			print(", ", end="")
	print("")

# Initialization

import random

random.seed(0)

def generate_random_points(n):
	return [(random.randint(-n*100, n*100), random.randint(-n*100, n*100)) for i in range(n)]

# Show analysis of algorithm

if len(sys.argv) > 1 and sys.argv[1] == "steps":
	show_steps()
	exit()

p = generate_random_points(100)

plot_points(p)


# Algorithm: Graham Scan

L = graham_scan(p)
plot_KP2(p, L, "Graham Scan")
print("Algorithm: Graham Scan: ")
print_points(L)

# Algorithm: Gift Wrapping

L = gift_wrapping(p)
plot_KP2(p, L, "Gift Wrapping")
print("Algorithm: Gift Wrapping: ")
print_points(L)

# Algorithm: Divide and Conquer

L = divide_and_conquer(p)
plot_KP2(p, L, "Divide and Conquer")
print("Algorithm: Divide and Conquer: ")
print_points(L)

# Algorithm: Quick Hull

L = quick_hull(p)
plot_KP2(p, L, "Quick Hull")
print("Algorithm: Quick Hull: ")
print_points(L)
