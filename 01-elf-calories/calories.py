with open('01-elf-calories/calories.txt') as file:
    calories = file.read()
    elf = calories.split("\n\n")
    most_calories = 0
    sum_calories = []
    for calories in elf:
        calories = calories.split("\n")
        total = sum(int(i) for i in calories)
        if total > most_calories:
            most_calories = total
        sum_calories.append(total)
            
    top_3 = sorted(sum_calories, reverse=True)[:3]
    top_3_sum = sum(top_3)

print('Most calories:',most_calories)
print('Top 3 calories:', *top_3, sep=' ')
print('Sum of top 3 calories:', top_3_sum)