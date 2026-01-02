import itertools
import numpy as np

def riemann_sum_nd(f, bounds, bins=10):
    """
    計算 n 維黎曼和
    :param f: 目標函數，接受一個長度為 n 的 list 或 array
    :param bounds: 積分邊界，格式為 [(a1, b1), (a2, b2), ..., (an, bn)]
    :param bins: 每個維度分割的段數
    """
    n = len(bounds)
    dims_axes = []
    delta_v = 1.0
    
    # 1. 準備每個維度的採樣點與計算 Delta V
    for a, b in bounds:
        dx = (b - a) / bins
        delta_v *= dx
        # 使用中點法 (Midpoint Rule) 採樣，精度較高
        offsets = np.linspace(a + dx/2, b - dx/2, bins)
        dims_axes.append(offsets)
    
    # 2. 生成所有維度的笛卡爾積 (Cartesian Product) 並加總
    total_sum = 0
    for point in itertools.product(*dims_axes):
        total_sum += f(point)
    
    return total_sum * delta_v

# --- 測試範例 ---
# 積分函數 f(x, y, z) = x + y + z
# 積分區域為 [0, 1] x [0, 1] x [0, 1]
def my_func(x_vec):
    return sum(x_vec)

bounds = [(0, 1), (0, 1), (0, 1)] # n = 3
result = riemann_sum_nd(my_func, bounds, bins=20)
print(f"黎曼和計算結果 (n=3): {result:.6f}") # 理論值應為 1.5
from scipy.integrate import nquad

def professional_nd_integral(f, bounds):
    """
    使用 SciPy 計算 n 維數值積分
    :param f: 函數，定義為 f(x1, x2, ..., xn)
    :param bounds: 積分範圍 [(a1, b1), (a2, b2), ...]
    """
    # nquad 要求 bounds 的順序與參數順序一致
    # 注意：nquad 的函數簽名是 f(x1, x2, ..., xn)，與上面的 list 輸入略有不同
    result, error = nquad(f, bounds)
    return result, error

# --- 測試範例 ---
def my_func_scipy(x, y, z):
    return x + y + z

bounds = [(0, 1), (0, 1), (0, 1)]
val, err = professional_nd_integral(my_func_scipy, bounds)
print(f"SciPy 計算結果: {val:.6f}, 誤差估計: {err:.2e}")
