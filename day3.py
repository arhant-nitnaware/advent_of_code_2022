with open('input_day3.txt', 'r') as file:
    text = file.read()
data = text.split()

def cpr(a):
    if ord(a) - 96 > 0:
        return (ord(a) - 96)
    else:
        return (ord(a) - 38)
    
t_pri = 0
for bag in data:
    cp1, cp2 = set(bag[:int((len(bag)/2))]), set(bag[int((len(bag)/2)):])
    for item in cp1:
        if item in cp2:
            t_pri += cpr(item)
print(t_pri)