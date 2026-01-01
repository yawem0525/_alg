### 貪婪法
def greedy_sum(nums):
    total = 0
    for n in sorted(nums, reverse=True):
        if total + n <= 10:
            total += n
    return total

print(greedy_sum([7, 5, 3, 2, 1]))
