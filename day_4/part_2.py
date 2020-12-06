import re

def validate_hcl(value):
    return re.match(r'^#([0-9]|[a-f]){6}$', value)

def validate_ecl(value):
    return re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', value)

def validate_pid(value):
    return re.match(r'^[0-9]{9}$', value)

def validate_yr(value, min, max):
    return value.isnumeric() and int(value) >= min and int(value) <= max

def validate_hgt(value):
    return re.match(r'^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$', value)

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
            if validate_yr(p['byr'], 1920, 2002) \
            and validate_yr(p['iyr'], 2010, 2020) \
            and validate_yr(p['eyr'], 2020, 2030) \
            and validate_hcl(p['hcl']) \
            and validate_ecl(p['ecl']) \
            and validate_pid(p['pid']) \
            and validate_hgt(p['hgt']):
                count+=1
    
    print(count)

