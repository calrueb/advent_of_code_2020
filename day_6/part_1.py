with open('input.txt') as f:
    # store unique answers in set to handle dups by default
    answers = set()
    total = 0
    while True:
        line = f.readline()
        if line == '\n' or not line:
            total += len(answers)
            answers = set()

            if not line:
                break

        for c in line.strip():
            answers.add(c)
        
    print(total)