"""
[S]                 [T] [Q]        
[L]             [B] [M] [P]     [T]
[F]     [S]     [Z] [N] [S]     [R]
[Z] [R] [N]     [R] [D] [F]     [V]
[D] [Z] [H] [J] [W] [G] [W]     [G]
[B] [M] [C] [F] [H] [Z] [N] [R] [L]
[R] [B] [L] [C] [G] [J] [L] [Z] [C]
[H] [T] [Z] [S] [P] [V] [G] [M] [M]
 1   2   3   4   5   6   7   8   9 
"""

blocks = [["H","R","B","D","Z","F","L","S"],
          ["T","B","M","Z","R"],
          ["Z","L","C","H","N","S"],
          ["S","C","F","J"],
          ["P","G","H","W","R","Z","B"],
          ["V","J","Z","G","D","N","M","T"],
          ["G","L","N","W","F","S","P","Q"],
          ["M","Z","R"],
          ["M","C","L","G","V","R","T"]]

with open("in") as x:
    y = x.read().split("\n")
    for i in y:
        z = i.split(" ")
        move = int(z[1])-1
        _from = int(z[3])-1
        to = int(z[5])-1
        for i in range(move+1):
            tmp = blocks[int(_from)].pop()
            blocks[int(to)].append(tmp)
    for i in blocks:
        print(i.pop(), end="")
    print()