f = open("day1.txt", "r")
total = 0
for sentence in f:
    first = last = 0

    for d in sentence:
        if d.isdigit():
            if not first:
                first = d
            last = d
    total = total + (int(first + last))

print(total)
f.close()
