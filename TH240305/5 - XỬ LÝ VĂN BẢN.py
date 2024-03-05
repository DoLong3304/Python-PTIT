docs = []

while True:
    try:
        docs += input().lower().split()
    except EOFError:
        break

para = []
s = []
for d in docs:
    mark = False
    for c in d:
        if c in '.?!':
            mark = True
            break
    if mark:
        s.append(d[:-1])
        para.append(' '.join(s).capitalize())
        s = []
    else:
        s.append(d)

for p in para:
    print(p)