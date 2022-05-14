## Calculate percentage of games won by a baseball team.
name = input("Enter name of team: ")
gamesWon = int(input("Enter number of games won: "))
gamesList = int(input("Enter number of games lost: "))
percentageWon = round(100 * (gamesWon) / (gamesWon + gamesList), 1)
print(name, "won", str(percentageWon) + '%', "of their games.")