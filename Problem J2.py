# The first line of input consists of a positive integer N representing the total number of players
# on the team. This is followed by a pair of consecutive lines for each player. The first line
# in a pair is the number of points that the player scored. The second line in a pair is the
# number of fouls that the player committed. Both the number of points and the number of
# fouls, are non-negative integers.

numPlayers = int(input())
stars = 0

for x in range(0,numPlayers):
    points = int(input())
    fouls = int(input())
    score = points * 5 - fouls * 3
    if score > 40:
        stars += 1

if stars == numPlayers:
    print(f"{stars}+")
else:
    print(stars)
