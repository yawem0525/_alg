### 梯度下降法
def gradient_descent(lr=0.1, iters=100):
    x = 0
    for _ in range(iters):
        grad = 2 * (x - 3)
        x -= lr * grad
    return x

print(gradient_descent())
