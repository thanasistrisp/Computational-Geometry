from algorithms.graham_scan import graham_scan
from algorithms.gift_wrapping import gift_wrapping
from algorithms.divide_and_conquer import divide_and_conquer
from algorithms.quick_hull import quick_hull

import random
import time

random.seed(0)

def generate_random_points(n):
	return [(random.randint(-n*100, n*100), random.randint(-n*100, n*100)) for i in range(n)]

for i in [100, 1000, 10000, 100000, 1000000]:
	p = generate_random_points(i)
	
	print("n = " + str(i))

	start = time.time()
	graham_scan(p)
	end = time.time()
	print("Graham Scan: " + str(round(end-start, 2)))

	start = time.time()
	gift_wrapping(p)
	end = time.time()
	print("Gift Wrapping: " + str(round(end-start, 2)))

	start = time.time()
	divide_and_conquer(p)
	end = time.time()
	print("Divide and Conquer: " + str(round(end-start, 2)))

	start = time.time()
	quick_hull(p)
	end = time.time()
	print("Quick Hull: " + str(round(end-start, 2)))

	print("--------------------")
