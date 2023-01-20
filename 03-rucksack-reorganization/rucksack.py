with open("03-rucksack-reorganization/rucksacks_contents.txt") as file:
    contents = file.read()
    contents = contents.split("\n")
    priorities_sum = 0
    for rucksack in contents:
        rucksack = rucksack.split("\n")
        rucksack = ' '.join(rucksack)
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]
        match_items = []        
        for item in first_compartment:
            if item in second_compartment:
                match_items.append(item)
        for item in set(match_items):
            if item.isupper():
                priorities_sum += (ord(item) - 38)
            else:
                priorities_sum += (ord(item) - 96)
    print('Priorities sum:',priorities_sum)