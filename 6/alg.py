with open("in") as i:
    p = list(i.read())
    total = 0
    chars = 0
    _chars = []
    for i in p:
        if chars == 4:
            print(_chars)
            print(total)
            exit(1)
        if i not in _chars:
            chars += 1
            _chars.append(i)
        else:
            _chars = []
            chars = 0
        total += 1