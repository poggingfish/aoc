import string
sum = 0
totals = {}
for i in string.ascii_letters:
    totals[i] = 0
with open("in") as i:
    for x in i.read().split("\n"):
        x1 = x[0:int(len(x)/2)]
        x2 = x[int(len(x)/2):len(x)]
        a=list(set(x1)&set(x2))
        totals[a[0]] += string.ascii_letters.find(a[0])+1
for i in totals:
    sum += totals[i]
print(sum)