with open('input.txt') as file:
    # Parse input
    raw_input = file.read()
    grid = [[c for c in line] for line in raw_input.splitlines()]

    # Traverse grid
    trees = 0
    loc = {'x': 0, 'y': 0}
    while (loc['y']< len(grid)):
        # print(f"pre: {loc}, val: {grid[loc['y']][loc['x']]}" )
        if grid[loc['y']][loc['x']] == '#':
            trees += 1
        loc['x'] = (loc['x'] + 3) % len(grid[1])
        loc['y'] += 1

        # print(f'updated: {loc}')

    print(trees)



