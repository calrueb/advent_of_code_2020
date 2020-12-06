with open('input.txt') as f:

    group_answers = None
    total = 0
    while True:
        line = f.readline()
        if line == '\n' or not line:
            total += len(group_answers)
            group_answers = None
            if not line:
                break
        else: 
            personal = set()
            for c in line.strip():
                personal.add(c)
            
            if group_answers == None:
                group_answers = personal
            else:
                # Get set intersection
                group_answers = group_answers & personal
    
    print(total)



