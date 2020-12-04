# Goal: Write a script that finds two numbers in a list that sum to 2020 and return those numbers multiplied together.

# Data lives at https://adventofcode.com/2020/day/1/input
with open('inputs.txt') as f:
    unprocessed_values = f.read().split()
    values = [int(string_num) for string_num in unprocessed_values]
    # This could be more efficent but since it is in the order of 10s of values I will brute force
    for i in range(len(values)):
        for j in range(1, len(values)):
            if values[i] + values[j] == 2020:
                print(f'Values: ({values[i]}, {values[j]})')
                print(f'Answer: {values[i] * values[j]}')
                exit()

    print('No pair found')
