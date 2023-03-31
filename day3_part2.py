with open('input_day3.txt', 'r') as file:
    text = file.read()
data = text.split()

def cpr(a):
    if ord(a) - 96 > 0:
        return (ord(a) - 96)
    else:
        return (ord(a) - 38)

total = 0
n = 0
while True:
    #print(n)
    for x in set(data[n]):
        if x in set(data[n+1]) and x in set(data[n+2]):
            print(x)
            total += cpr(x)
    n += 3
    if n == 300:
        break
print(total)