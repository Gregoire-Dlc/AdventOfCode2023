import re
f = open('day4.txt', 'r')

total = 0
for sentence in f:
    parts = sentence.split(':')[1].split('|')
    winners  = [m.strip() for m in re.findall(r'\d+', parts[0])]
    numbers =  [m.strip() for m in re.findall(r'\d+', parts[1])]
    indice = len([win for win in winners if win in numbers])
    total += pow(2, indice-1) if indice else 0
print(total)
f.close()
