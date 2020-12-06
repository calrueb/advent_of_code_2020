
def run():
    with open('input.txt') as file:
        # Parse input
        raw_input = file.read()
        grid = [[c for c in line] for line in raw_input.splitlines()]

        total = 1

        slopes = [
            {'x': 1, 'y': 1},
            {'x': 3, 'y': 1},
            {'x': 5, 'y': 1},
            {'x': 7, 'y': 1},
            {'x': 1, 'y': 2}
        ]

        for slope in slopes:
            total *= calculate_run(grid, slope)

        print(total)



def calculate_run(grid, slope):
    trees = 0
    loc = {'x': 0, 'y': 0}
    while (loc['y']< len(grid)):
        # print(f"pre: {loc}, val: {grid[loc['y']][loc['x']]}" )
        if grid[loc['y']][loc['x']] == '#':
            trees += 1
        loc['x'] = (loc['x'] + slope['x']) % len(grid[1])
        loc['y'] += slope['y']

        # print(f'updated: {loc}')

    return trees


run()