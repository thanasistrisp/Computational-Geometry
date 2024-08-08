from algorithms.orthogonal_search import *
from numpy import random
from matplotlib import pyplot as plt

np.random.seed(0)

# employ has a tuple of (name, salary, age)

def generate_employee(n):
    """
    @param n: number of employees
    return: list of employees
    """
    employees = []
    for _ in range(n):
        name = ''
        for _ in range(10):
            name += chr(random.randint(97, 123))
        salary = random.randint(1000, 10000)
        age = random.randint(20, 60)
        employees.append((name, salary, age))
    return employees

employees = generate_employee(1000)
employees = np.array(employees)
employees_copy = employees.copy()
# delete name column
employees_copy = np.delete(employees_copy, 0, 1)
employees_copy = employees_copy.astype(int)

# query employee with salary between 2000 and 3000 and age between 30 and 40
rec = Rectangle(2000, 3000, 30, 40)
result = rectangle_search(employees_copy, rec)

# plot
plt.scatter(employees_copy[:, 0], employees_copy[:, 1])
plt.plot([rec.x1, rec.x2], [rec.y1, rec.y1], color='y')
plt.plot([rec.x1, rec.x2], [rec.y2, rec.y2], color='y')
plt.plot([rec.x1, rec.x1], [rec.y1, rec.y2], color='y')
plt.plot([rec.x2, rec.x2], [rec.y1, rec.y2], color='y')

for i in result:
    plt.scatter(i[0], i[1], color='r')

plt.xlabel('salary')
plt.ylabel('age')
plt.title('Employee Search')

plt.show()

# print employees with names
for i in result:
    print(employees[np.where((employees_copy == i).all(axis=1))])




from scipy.spatial import KDTree

tree = KDTree(employees_copy)
dist, ind = tree.query([2000, 30], k=10)
# plot neighbors
plt.scatter(employees_copy[:, 0], employees_copy[:, 1])
plt.scatter(2000, 30, color='r')
plt.scatter(employees_copy[ind, 0], employees_copy[ind, 1], color='y')
plt.xlabel('salary')
plt.ylabel('age')
plt.title('Employee Neighbors')
plt.show()
print(employees[ind])
