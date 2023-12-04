import re
f = open('day3.txt', 'r')
engine = f.readlines()

total = 0
symboles = re.findall(r'[^0-9.\n]', ''.join(engine))
for i in range(0, len(engine)):
    for e in re.finditer(r'\d+', engine[i]):
        if e.start() > 0 and engine[i][e.start()-1] in symboles:
            total += int(e.group())
        elif e.end() < len(engine[i]) and engine[i][e.end()] in symboles:
            total += int(e.group())
        elif i > 0 and any(char in symboles for char in engine[i-1][e.start()-1 if e.start() > 0 else e.start():e.end()+1 if e.end() < len(engine[i]) else e.end()]):
            total += int(e.group())
        elif i < len(engine)-1 and any(char in symboles for char in engine[i+1][e.start()-1 if e.start() > 0 else e.start():e.end()+1 if e.end() < len(engine[i]) else e.end()]):
            total += int(e.group())
print(total)
f.close()
