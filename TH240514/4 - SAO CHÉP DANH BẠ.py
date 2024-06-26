class Phone:
    def __init__(self, date, name, phone):
        self.date = date
        self.name = name
        self.phone = phone
        self.firstname = name.split()[-1]

    def __str__(self):
        return f'{self.name}: {self.phone} {self.date}'


f1 = open("SOTAY.txt", 'r')
x = []
for i in f1.read().split('\n'):
    if len(i) > 0:
        x.append(i)
a, date, i = [], '', 0
while i < len(x) - 1:
    if x[i][:4] == 'Ngay':
        date = x[i][5:]
        i += 1
    else:
        a.append(Phone(date, x[i], x[i + 1]))
        i += 2
a.sort(key=lambda x: (x.firstname, x.name))
f1.close()
f2 = open("DIENTHOAI.txt", 'w')
for i in a:
    f2.write(i.__str__() + '\n')
f2.close()