with open('input_day2.txt', 'r') as file:
    text = file.read()

data = (text.replace(' ', '')).split('\n')
data.pop()

def check(p1,p2):
    score = 0
    if p2 == 'X':
        if p1 == 'A':
            score += 3 + 0
        elif p1 == 'B':
            score += 1 + 0
        elif p1 == 'C':
            score += 2 + 0
    elif p2 == 'Y':
        if p1 == 'A':
            score += 1 + 3
        elif p1 == 'B':
            score += 2 + 3
        elif p1 == 'C':
            score += 3 + 3
    elif p2 == 'Z':
        if p1 == 'A':
            score += 2 + 6
        elif p1 == 'B':
            score += 3 + 6
        elif p1 == 'C':
            score += 1 + 6
    print(score)
    return score

my_score = 0
for match in data:
    my_score += check(match[0], match[1])
print(my_score)