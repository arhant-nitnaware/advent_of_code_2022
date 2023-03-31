with open('input_day1.txt', 'r') as file:
    text = file.read()

data = text.split('\n\n')
print(data)

max_cal = 0
for raindeer in data:
    cal = 0
    raindeer_data = raindeer.split('\n')
    for item in raindeer_data:
        if item != '':
            cal = cal + int(item)
        else:
            None   
    if cal > max_cal:
        max_cal = cal

print(max_cal)