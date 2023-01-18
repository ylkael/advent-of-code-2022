with open('01-elf-calories/calories.txt') as file:
    calories = file.read()
    elf = calories.split("\n\n")
    most_calories = 0
    for calories in elf:
        calories = calories.split("\n")
        total= sum(int(i) for i in calories)
        if total > most_calories:
            most_calories = total
        
print('Most calories:',most_calories)