import re
f = open('day4.txt', 'r')
file = f.readlines()

coeffs = {col:1 for col in range(0, len(file))}
for key, sentence in enumerate(file):
    parts = sentence.split(':')[1].split('|')
    winners  = [m.strip() for m in re.findall(r'\d+', parts[0])]
    numbers =  [m.strip() for m in re.findall(r'\d+', parts[1])]
    indice = len([win for win in winners if win in numbers])
    for i in range(1, indice+1):
        coeffs[key+i] += coeffs[key]
print(sum(coeffs.values()))
f.close()
