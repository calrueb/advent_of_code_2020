# Goal: Similar to part one, but now it is three numbers

# Data lives at https://adventofcode.com/2020/day/1/input
with open('inputs.txt') as f:
    unprocessed_values = f.read().split()
    values = [int(string_num) for string_num in unprocessed_values]
    # This could be more efficent but since there are in the order of 10s of values I will brute force
    for i in range(len(values)):
        for j in range(1, len(values)):
            for k in range(2, len(values)):
                if values[i] + values[j] + values[k] == 2020:
                    print(f'Values: ({values[i]}, {values[j]}, {values[k]})')
                    print(f'Answer: {values[i] * values[j] * values[k]}')
                    exit()

    print('No triplet found')
