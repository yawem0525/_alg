import random

def f(x):
    return -(x - 3) ** 2 + 10

def hill_climbing(start, step=0.1, max_iter=100):
    x = start
    for _ in range(max_iter):
        neighbors = [x - step, x + step]
        best = max(neighbors, key=f)
        if f(best) <= f(x):
            break
        x = best
    return x, f(x)

if __name__ == "__main__":
    result = hill_climbing(random.uniform(-10, 10))
    print(result)
