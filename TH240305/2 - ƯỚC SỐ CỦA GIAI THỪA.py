for _ in range(int(input())):
    n, p = map(int, input().split())
    x = 0
    for i in range (2, n + 1):
        m = i
        while m % p == 0:
            m //= p
            x += 1
    print(x)