import re
from functools import reduce
f = open('day3.txt', 'r')
engine = f.readlines()

total = 0
for i in range(0, len(engine)):
    for e in re.finditer(r'[*]', engine[i]):
        numbers = []
        previous_line = re.finditer(r'\d+', engine[i-1]) if i > 0 else []
        actual_line = re.finditer(r'\d+', engine[i])
        next_line = re.finditer(r'\d+', engine[i+1]) if i < len(engine)-1 else []
        for digit in actual_line:
            if digit.end() == e.start() or digit.start() == e.end():
                numbers.append(int(digit.group()))
        for digit in previous_line:
            if digit.end() == e.start() or digit.start() == e.end() or digit.start() <= e.start() <= digit.end():
                numbers.append(int(digit.group()))
        for digit in next_line:
            if digit.end() == e.start() or digit.start() == e.end() or digit.start() <= e.start() <= digit.end():
                numbers.append(int(digit.group()))
        total += reduce(lambda x, y: x * y, numbers) if len(numbers) >= 2 else 0
print(total)
f.close()
