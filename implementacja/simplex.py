import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the system of inequalities
# x1 + x2 <= 4
# 2x1 + x2 <= 5
# x1, x2 >= 0
A = [[1, 1], [2, 1]]
b = [4, 5]
x0_bounds = (0, None)
x1_bounds = (0, None)

# Define the objective function
# z = -x1 - 2x2
c = [-1, -2]

# Solve the problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method="simplex")

# Visualization
x = np.linspace(0, 4, 100)
y1 = 4 - x
y2 = (5 - 2 * x) / 1
plt.plot(x, y1, label="x1 + x2 <= 4")
plt.plot(x, y2, label="2x1 + x2 <= 5")
plt.xlim((0, 4))
plt.ylim((0, 4))
plt.xlabel("x1")
plt.ylabel("x2")
plt.fill_between(x, np.maximum(y1, y2), color="gray", alpha=0.5)
plt.scatter(res.x[0], res.x[1], color="r")
plt.legend()
plt.show()
