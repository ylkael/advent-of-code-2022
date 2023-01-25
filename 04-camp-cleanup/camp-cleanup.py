with open("04-camp-cleanup/assignment-pairs.txt") as file:
    content = file.read()
    contents = content.split("\n")
    print(contents)
    
    for pair in contents:
        pair = pair.split("\n")
        print('pair',pair)
        tasks = pair[0].split(",")

        for i in range(len(pair)):            
            elf1_tasks = tasks[i].split("-")
            for i in range(len(elf1_tasks)):
                elf1_tasks[i] = int(elf1_tasks[i])
            tasks1_range = []
            for i in range(elf1_tasks[0], elf1_tasks[1] + 1):
                tasks1_range.append(i)
            print('range1',elf1_tasks,':',tasks1_range)

            elf2_tasks = tasks[1].split("-")
            for i in range(len(elf2_tasks)):
                elf2_tasks[i] = int(elf2_tasks[i])
            tasks2_range = []
            for i in range(elf2_tasks[0], elf2_tasks[1] + 1):
                tasks2_range.append(i)
            print('range2',elf2_tasks,':',tasks2_range)


    
        # print('tasks',tasks)

        # task1 = tasks[0].split("-")
        # task2 = tasks[1].split("-")
        # print(task1)
        # print(task2)

        # for i in range(len(task1)):
        #     task1[i] = int(task1[i])
        # for i in range(task1[0], task1[1] + 1):
        #     print('tasks1:',i)
        # for i in range(len(task2)):
        #     task2[i] = int(task2[i])
        # for i in range(task2[0], task2[1] + 1):
        #     print('tasks2',i)
        # print(task1)
        # print(task2)



