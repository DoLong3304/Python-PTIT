from math import sqrt

for _ in range(int(input())):
    n = int(input()) * 2
    cnt = 0
    s = int(sqrt(n)) + 1
    for i in range(2, s):
        if n % i == 0:
            x = i + (n // i) - 1
            if x % 2 == 0:
                b = x // 2
                a = (n // i) - b
                if a >= 1 and b > a:
                    cnt += 1
    print(cnt)