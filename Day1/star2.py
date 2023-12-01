f = open("day1.txt", "r")
total = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for sentence in f:
    first = ifirst = last = ilast = 0

    # DIGITS
    for key, d in enumerate(sentence):
        if d.isdigit():
            if not first:
                first = d
                ifirst = key
            last = d
            ilast = key

    # WORDS
    for key, number in enumerate(numbers):
        if number in sentence:
            taille = len(sentence.split(number)[0])
            rtaille = len(sentence.rsplit(number,1)[0])
            if taille < ifirst:
                first = key + 1
                ifirst = taille
            if rtaille > ilast:
                last = key + 1
                ilast = rtaille
    total = total + (int(str(first) + str(last)))

print(total)
f.close()
