with open("04-camp-cleanup/assignment-pairs.txt") as file:
    content = file.read()
    contents = content.split("\n")
    assignments_overlap_full = 0
    assignments_overlap_at_all = 0    
    for pair in contents:
        pair = pair.split("\n")
        tasks = pair[0].split(",")
        for i in range(len(pair)):
            # Elf 1 tasks range            
            elf1_tasks = tasks[i].split("-")
            for i in range(len(elf1_tasks)):
                elf1_tasks[i] = int(elf1_tasks[i])
            elf1_tasks_range = []
            for i in range(elf1_tasks[0], elf1_tasks[1] + 1):
                elf1_tasks_range.append(i)
            # Elf 2 tasks range
            elf2_tasks = tasks[1].split("-")
            for i in range(len(elf2_tasks)):
                elf2_tasks[i] = int(elf2_tasks[i])
            elf2_tasks_range = []
            for i in range(elf2_tasks[0], elf2_tasks[1] + 1):
                elf2_tasks_range.append(i)
            # Part 1: Check if tasks overlap fully
            if set(elf1_tasks_range).issubset(elf2_tasks_range) or set(elf2_tasks_range).issubset(elf1_tasks_range):
                assignments_overlap_full += 1
            # Part 2: Check if tasks overlap at all
            if set(elf1_tasks_range).intersection(elf2_tasks_range) or set(elf2_tasks_range).intersection(elf1_tasks_range):
                assignments_overlap_at_all += 1
        
    print('Total assignment overlaps fully:',assignments_overlap_full)
    print('Total assignment overlaps at all:',assignments_overlap_at_all)
                
