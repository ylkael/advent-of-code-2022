scores = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3, # Scissors
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

outcome_round = {
    "lost": 0,
    "draw": 3,
    "won": 6,
}


with open("02-rock-paper-scissors/input.txt") as file:
    guide = file.read()
    strategy = guide.split("\n\n")

    total_score = 0
    score = 0

    for turn in strategy:
        turn = turn.split("\n")
        # print('t[0]',turn[0])
        # opponent = turn[0][0]
        # choise = turn[0][2]
        for i in turn:
            print(total_score)
            # print('i',i)
            opponent = i[0]
            you = i[2]
            # print('op',opponent)
            # print('ch',you)
            if scores[opponent] == scores[you]:
                total_score += scores[you] + outcome_round['draw']
                points = scores[you] + outcome_round['draw']
                score += points
                print('draw points',points)
                print(total_score)
                # print('draw 3p',opponent,you, scores[opponent],scores[you])
                print('score',total_score)
            elif scores[opponent] < scores[you]:
                points = scores[you] + outcome_round['won']
                score += points

                print('win points',points)
               
                total_score += scores[you] + outcome_round['won']
                print('you win 6+',opponent,you, scores[opponent],scores[you])
                print('score',total_score)
            else:
                points = scores[you] + outcome_round['lost']
                score += points

                print('lose points',points)            
                total_score += scores[you] + outcome_round['lost']
                print('you lose',opponent,you, scores[opponent],scores[you])
                print('score',total_score)

        
        print('total',total_score)
        print('score',score)
        
        # print('o',opponent)
        # print('c',choise)
        # total = sum(scores[i] for i in turn)
        # if total > most_points:
        #     most_points = total
        # sum_points.append(total)

    # top_3 = sorted(sum_points, reverse=True)[:3]
    # top_3_sum = sum(top_3)


