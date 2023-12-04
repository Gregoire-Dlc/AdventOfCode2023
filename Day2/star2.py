import re
from functools import reduce
f = open('day2.txt', 'r')

total = 0
for sentence in f:
    maximums = {"red": 0, "blue": 0, "green": 0}
    for color in maximums:
        maximums[color] = max([int(re.search(r'\d+', n).group()) for n in re.findall(r'\d+ ' + color, sentence)])
    total += reduce(lambda x, y: x * y, maximums.values())
print(total)
f.close()
