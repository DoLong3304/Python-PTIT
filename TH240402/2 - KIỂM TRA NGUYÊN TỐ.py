def isPrime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

n, m = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] = 1 if isPrime(a[i][j]) else 0

for i in a:
    print(*i)