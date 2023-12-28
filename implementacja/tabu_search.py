import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x**2 + y**2 + 2 * np.sin(x) - 9 * np.sin(y)


def tabu_search(start, tabu_list_size, max_iter):
    x, y = start
    best_score = f(x, y)
    tabu_list = [start]
    path = [start]

    for _ in range(max_iter):
        neighbors = [(x + dx, y + dy) for dx in [-0.1, 0, 0.1] for dy in [-0.1, 0, 0.1]]
        np.random.shuffle(neighbors)

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                score = f(*neighbor)
                if score < best_score:
                    best_score = score
                    x, y = neighbor
                    tabu_list.append(neighbor)
                    path.append(neighbor)
                    if len(tabu_list) > tabu_list_size:
                        tabu_list.pop(0)
                    break

    return x, y, best_score, path


x, y, best_score, path = tabu_search((5, 5), 10, 1000)

# Visualization
x_values = np.linspace(-10, 10, 100)
y_values = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = f(X, Y)

plt.figure(figsize=(10, 8))
plt.contourf(X, Y, Z, 110, cmap="viridis")
plt.plot(*(5, 5), "ro")  # start point
plt.plot(x, y, "bo")  # end point
plt.plot(*zip(*path), "w-")  # path
plt.colorbar()
plt.show()
