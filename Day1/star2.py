f = open('day1.txt', 'r')
total = 0
numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
for sentence in f:
    selected = []
    for key, d in enumerate(sentence):
        if d.isdigit():
            selected.append(d)
        for indice,number in numbers.items():
            if sentence.startswith(number,key):
                selected.append(str(indice))
    total = total + int(selected[0] + selected[-1])
print(total)
f.close()
