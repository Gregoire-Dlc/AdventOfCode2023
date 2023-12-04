import re
f = open('day2.txt', 'r')

total = 0
combinaison = {12: "red", 13: "green", 14: "blue"}
for sentence in f:
    correct = True
    for occ,color in combinaison.items():
        if(not all(int(re.search(r'\d+', n).group()) <= occ for n in re.findall(r'\d+ '+color,sentence))):
            correct = False
            break
    total += int(re.search(r'\d+', sentence).group()) if correct else 0
print(total)
f.close()
