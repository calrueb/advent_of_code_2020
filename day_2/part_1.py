with open('input.txt') as f:
    raw_input = f.read()
    # Parse input into array of tuples in the form (min, max, char, password)
    raw_input = raw_input.splitlines()
    raw_input = [i.split() for i in raw_input]
    clean = []
    for i in raw_input:
        clean.append((int(i[0].split('-')[0]),
                      int(i[0].split('-')[1]), i[1][:1], i[2]))

    # validate each entry
    num_valid = 0

    for password in clean:
        if password[3].count(password[2]) >= password[0] and password[3].count(password[2]) <= password[1]:
            num_valid += 1

    print(num_valid)
