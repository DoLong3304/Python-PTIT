for _ in range(int(input())):
    n = int(input())
    a = [x for x in input().split()]
    mp = {}
    for i in a:
        x = sum(map(int, list(i)))
        mp[i] = x
    mp = sorted(mp.items(), key=lambda x: (x[1], int(x[0])))
    for i in mp:
        print(i[0], end=' ')
    print()