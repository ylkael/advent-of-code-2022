with open("03-rucksack-reorganization/rucksacks_contents.txt") as file:
    contents = file.read()
    contents = contents.split("\n")
    groups = []
    match_items = []      
    priorities_sum = 0
    n=0
    for line in contents:
        groups.append(line)
        n+=1
        if n%3==0:
            dublicates = [] 
            i = 0
            while len(groups[0]) > i:
                if groups[0][i] in groups[1] and groups[0][i] in groups[2] and groups[0][i] not in dublicates:
                    dublicates.append(groups[0][i])
                    match_items.append(groups[0][i])
                i+=1
            groups = []

    for item in match_items:
        if item.isupper():
            priorities_sum += (ord(item) - 38)
        else:
            priorities_sum += (ord(item) - 96)

print('Priorities sum:',priorities_sum)