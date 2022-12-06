"""
Rock score: 1
Your rock: X
Opponent rock: A

Paper score: 2
Your paper: Y
Opponent paper: B

Scissors score: 3
Your scissors: C
Opponent scissors: Z

Winning score: 6
Draw: 3
Lose: 0
"""

beats = {
    "scissors": "paper",
    "rock": "scissors",
    "paper": "rock"
}
def gameState(opp,you):
    if opp == you:
        return "draw"
    if beats[opp] == you:
        return "lose"
    else:
        return "win"
score = 0
with open("in") as i:
    for x in i.read().split("\n"):
        x = x.split(" ")
        x = eval(str(x).replace("X","rock").replace("A","rock")
                 .replace("C", "scissors"). replace("Z","scissors")
                 .replace("Y","paper"). replace("B","paper"))
        if x[1] == "rock": score += 1
        if x[1] == "paper": score += 2
        if x[1] == "scissors": score += 3
        x = gameState(x[0],x[1])
        if x == "draw":
            score += 3
        if x == "win":
            score += 6
print(score)