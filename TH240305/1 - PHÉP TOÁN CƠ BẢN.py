def operator(a: int, b: int, c: int, _: str) -> bool:
    if _ == '+':
        return a + b == c
    if _ == '-':
        return a - b == c
    if _ == '*':
        return a * b == c
    if _ == '/':
        return a / b == c
    
def calculate(A: list, B: list, C: list, OP: list) -> str:
    for x in A:
        for y in B:
            for z in C:
                for _ in OP:
                    if operator(x, y, z, _):
                        return f'{x} {_} {y} = {z}'
    return 'WRONG PROBLEM!'

def limit(x: str) -> list:
    if x == '??':
        return range(10,100)
    elif x[0] == '?':
        return [i * 10 + int(x[1]) for i in range(1,10)]
    elif x[1] == '?':
        return [int(x[0]) * 10 + i for i in range(0,10)]
    else:
        return [int(x)]

for t in range(int(input())):
    problem = input().split()
    a, b, c = map(limit, problem[0::2])
    _ = ['+', '-', '*', '/'] if problem[1] == '?' else [problem[1]]
    print(calculate(a, b, c, _))