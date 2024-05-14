n = int(input())
a = [[int(x) for x in input().split()] for _ in range(n)]
k = int(input())

upper = lower = 0
for i in range(n-1):
    for j in range(n-i-1):
        upper += a[i][j]

for i in range(1, n):
    for j in range(n - i, n):
        lower += a[i][j]

res = abs(upper - lower)
print("YES" if res <= k else "NO")
print(res)