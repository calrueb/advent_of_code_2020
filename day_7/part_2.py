# Recursively go through all inner bags to get total count
def get_bags_inside(bag_dict, color):
    if len(bag_dict[color]) == 0:
        return 0
    
    total = 0
    for tup in bag_dict[color]:
        total += tup[1] + (get_bags_inside(bag_dict, tup[0]) * tup[1])
    
    return total 

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
            child_bags = [(b[1] + ' ' + b[2], int(b[0])) for b in [bag.strip().split() for bag in line.split('bags', 1)[1].strip()[8:-1].split(',')]]
            bag_map[parent_bag] = child_bags
        else:
            bag_map[parent_bag] = []
   
    print(get_bags_inside(bag_map, 'shiny gold'))

