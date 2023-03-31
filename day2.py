with open('input_day2.txt', 'r') as file:
    text = file.read()

data = (text.replace(' ', '')).split('\n')
data.pop()

def check(p1, p2): #p1 opponent, p2 me
    score = 0
    if p1 == 'A':
        if p2 == 'X':
            score = score + 1 + 3
        if p2 == 'Y':
            score = score + 2 + 6
        if p2 == 'Z':
            score = score + 3 + 0
    
    elif p1 == 'B':
        if p2 == 'X':
            score = score + 1 + 0
        if p2 == 'Y':
            score = score + 2 + 3
        if p2 == 'Z':
            score = score + 3 + 6
    
    elif p1 == 'C':
        if p2 == 'X':
            score = score + 1 + 6
        if p2 == 'Y':
            score = score + 2 + 0
        if p2 == 'Z':
            score = score + 3 + 3
    return score

my_score = 0
for match in data:
    my_score += check(match[0], match[1])
print(my_score)