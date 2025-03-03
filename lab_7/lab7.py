from functools import lru_cache

@lru_cache(maxsize=None)
def f(s, n):
    if n == 0:
        return 1
    if s == "0":
        return f("1", n-1)
    d = len(s)
    if d % 2 == 0:
        left = s[:d//2]
        right = s[d//2:]
        left_str = left.lstrip('0') if left.lstrip('0') else "0"
        right_str = right.lstrip('0') if right.lstrip('0') else "0"
        return f(left_str, n-1) + f(right_str, n-1)
    else:
        k = int(s)
        new_s = str(k * 2024)
        return f(new_s, n-1)

initial_stones = ["2701", "64945", "0", "9959979", "93", "781524", "620", "1"]
total_25 = sum(f(s, 25) for s in initial_stones)
total_75 = sum(f(s, 75) for s in initial_stones)

print(total_25) # 198075
print(total_75) # 235571309320764
