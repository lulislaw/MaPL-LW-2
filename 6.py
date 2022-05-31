pi = 3
const = 2
for a in range(15):
    i = a+1
    if (i % 2 == 0):
        pi = pi - (4 / (const*(const+1)*(const+2)))
        print(i,pi)
    else:
        pi = pi + (4 / (const*(const+1)*(const+2)))
        print(i, pi)
    const = const + 2