n = int(input())
a = []
for _ in range(n):
    s = input()
    c, t = map(int, input().split())
    a.append((s, c, t))
a.sort(key=lambda x: (-x[1], x[2], x[0]))
for i in a:
    print(*i)