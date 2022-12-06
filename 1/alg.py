totals = []
with open("in") as i:
    for x in i.read().split("\n\n"):
        totals.append(0)
        for y in x.split("\n"):
            totals[len(totals)-1] += int(y)
totals.sort()
print(totals)