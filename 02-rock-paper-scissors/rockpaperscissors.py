points = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3, # Scissors
    "lost": 0,
    "draw": 3,
    "win": 6,
}

win_moves = {
    "A": "Y", # Rock vs Paper
    "B": "Z", # Paper vs Scissors
    "C": "X", # Scissors vs Rock
}

draw_moves = {
    "A": "X", # Rock vs Rock
    "B": "Y", # Paper vs Paper
    "C": "Z", # Scissors vs Scissors
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
            if ((opponent,you) in win_moves.items()): 
                total_points += points[you] + points['win']            
            elif ((opponent,you) in draw_moves.items()): 
                total_points += points[you] + points['draw']
            else: 
                total_points += points[you] + points['lost']
        
    print('Total points:',total_points)
