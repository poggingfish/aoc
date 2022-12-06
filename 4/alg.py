t = 0
with open("in") as x:
    for i in x.read().split("\n"):
        p = i.split(",")
        y = range(int(p[0].split("-")[0]),int(p[0].split("-")[1])+1)
        z = range(int(p[1].split("-")[0]),int(p[1].split("-")[1])+1)
        if all(item in z for item in y): t+=1
        if all(item in z for item in y) == False: 
            if all(item in y for item in z): t += 1
print(t)