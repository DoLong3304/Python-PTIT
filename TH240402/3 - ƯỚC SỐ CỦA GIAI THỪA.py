for _ in range(int(input())):
    n, p = map(int, input().split())
    x = 0
    for i in range(2, n + 1):
        tmp = i
        while tmp % p == 0:
            x += 1
            tmp //= p
    print(x)