### 改良法
import random

def improved_hill_climbing(restarts=10):
    best = None
    for _ in range(restarts):
        x, value = hill_climbing(random.uniform(-10, 10))
        if best is None or value > best[1]:
            best = (x, value)
    return best

print(improved_hill_climbing())
