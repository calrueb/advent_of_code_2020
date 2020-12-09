with open('input.txt') as f:
    # Parse and put everything in a map
    bag_map = dict()
    while True:
        line = f.readline()
        if not line:
            break

        parent_bag = line.split('bags', 1)[0].strip()
        if line.split('bags', 1)[1].strip() != 'contain no other bags.':
            # This is some pretty unreadable string splitting code to get array of bag colors
            # I am making the assuming # of bags <= 9
            child_bags = [b[1] + ' ' + b[2] for b in [bag.strip().split() for bag in line.split('bags', 1)[1].strip()[8:-1].split(',')]]
            bag_map[parent_bag] = child_bags
    
    # Now that we have a mapping we can go through the map and find all bags that hold gold
    colors_to_check = ['shiny gold']
    checked_colors = set()
    while len(colors_to_check) > 0:
        for k, v in bag_map.items():
            if colors_to_check[0] in v: 
                if k not in checked_colors:
                    colors_to_check.append(k)
        checked_colors.add(colors_to_check[0])
        colors_to_check = colors_to_check[1:]

    # subtract 1 to account for shiny gold
    print(len(checked_colors) -1)

        

