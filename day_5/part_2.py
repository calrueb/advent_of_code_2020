def calculate_seat_id(ticket):
    lower_row = 0
    upper_row = 127
    for i in range(7):
        if ticket[i] == 'B':
            lower_row = upper_row - ((upper_row - lower_row) //2)
        else:
            upper_row = lower_row + ((upper_row - lower_row) // 2)

    if (upper_row != lower_row):
        print(f'ERROR-{lower_row},{upper_row}')
        exit()

    row = lower_row

    lower_seat = 0
    upper_seat = 7
    for i in range(3):
        if ticket[i+7] == 'R':
            lower_seat = upper_seat - ((upper_seat - lower_seat) //2)
        else:
            upper_seat = lower_seat + ((upper_seat - lower_seat) // 2)

    if (upper_seat != lower_seat):
        print(f'ERROR-{lower_seat},{upper_seat}')
        exit()

    seat = lower_seat
    return (row * 8) + seat


with open('input.txt') as f:
    line = f.readline()

    max_id = -1
    seats = []
    while True:
        seat_id = calculate_seat_id(line)

        seats.append(seat_id)
        
        line = f.readline()
        if(not line):
            break
  
    seats.sort()

    for i in range(1, len(seats)):
        if (seats[i] -1 != seats[i-1]):
            print(seats[i]-1)