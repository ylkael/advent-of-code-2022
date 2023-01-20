points = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors
    "lose": 0,
    "draw": 3,
    "win": 6,
}

win_moves = {
    "A": "B", # Rock vs Paper
    "B": "C", # Paper vs Scissors
    "C": "A", # Scissors vs Rock
}

lose_moves = {
    "A": "C", # Rock vs Scissors
    "B": "A", # Paper vs Rock
    "C": "B", # Scissors vs Paper
}

outcomes = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

with open("02-rock-paper-scissors/strategy_guide.txt") as file:
    guide = file.read()
    strategy = guide.split("\n\n")
    total_points = 0
    for turn in strategy:
        turn = turn.split("\n")
        for i in turn:
            opponent = i[0]
            you = i[2]
            choose = {}
            if outcomes[you] == "lose":
                choose[opponent] = lose_moves[opponent]
                you = choose[opponent]
                total_points += points[you] + points['lose']
            elif outcomes[you] == "draw":
                you = opponent
                total_points += points[you] + points['draw']
            else:
                choose[opponent] = win_moves[opponent]
                you = choose[opponent]
                total_points += points[you] + points['win']
        
    print('Total points:',total_points)
