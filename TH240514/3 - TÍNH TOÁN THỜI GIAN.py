class Gamer:
    def __init__(self, id, name, start, end) -> None:
        self.id = id
        self.name = name 
        self.start = start 
        self.end = end
    def time(self):
        s = self.start
        e = self.end
        h = e[0] - s[0]
        m = e[1] - s[1]
        if e[1] < s[1]:
            h -= 1
            m += 60
        return (h, m)
    def __str__(self) -> str:
        return f"{self.id}  {self.name} {self.time()[0]} gio {self.time()[1]} phut"
    
a = []
for _ in range(int(input())):
    id = input()
    name = input()
    start = tuple(map(int, input().split(':')))
    end = tuple(map(int, input().split(':')))
    a.append(Gamer(id, name, start, end))
a.sort(key=lambda x: (-x.time()[0], -x.time()[1]))
for i in a:
    print(i)