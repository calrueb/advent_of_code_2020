with open('input.txt') as file:
    # Parse input
    line = file.readline()
    passports = []
    current_passport = {}
    while line:
        # start a new passport
        if (line == '\n'):
            passports.append(current_passport)
            current_passport = {}
        else:
            attributes = [attr.strip() for attr in line.split(' ')]
            for attr in attributes:
                val = attr.split(':')
                current_passport[val[0]] = val[1]

        line = file.readline()
    
    # Add last passport
    passports.append(current_passport)
    # Validate
    count = 0
    for p in passports:
        if set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']).issubset(p.keys()):
            count += 1

    print(count)

