words = {}

for _ in range(int(input())):
    s = input().lower() + ' '
    x = ''
    for i in s:
        if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
            x += i
        elif x != '':
            if x in words:
                words[x] += 1
            else:
                words[x] = 1
            x = ''

words = sorted(words.items(), key=lambda x: (-x[1], x[0]))
for w, i in words:
    print(w, i)