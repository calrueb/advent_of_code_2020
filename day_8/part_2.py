# I am going to brute force this...
def run():
    with open('input.txt') as f:
        file_contents = f.read()
        for i in range(len(file_contents.split('\n'))):
            instruction_set = [(i.split(), False) for i in file_contents.split('\n')]
            if instruction_set[i][0][0] in ('nop', 'jmp'):
                # swap and run
                swapped = None
                if instruction_set[i][0][0] == 'nop':
                    swapped = 'jmp'
                else:
                    swapped = 'nop'
                instruction_set[i] = ([swapped, instruction_set[i][0][1]],False)
                result = process_intruction(0, instruction_set, 0)
                if result[0]:
                    print(f'Answer: {result[1]}')
                    break


def process_intruction(i_index, instruction_set, accumulator):
    if i_index >= len(instruction_set):
        return True, accumulator
    
    # If we have seen the instruction before it is time to exit the loop
    if instruction_set[i_index] == 'visited':
        return False, accumulator

    if instruction_set[i_index][0][0] == 'nop':
        instruction_set[i_index] = 'visited'
        return process_intruction(i_index + 1, instruction_set, accumulator)
    if instruction_set[i_index][0][0] == 'acc':
        inc = process_number_str(instruction_set[i_index][0][1])
        instruction_set[i_index] = 'visited'
        return process_intruction(i_index + 1, instruction_set, accumulator + inc) 
    if instruction_set[i_index][0][0] == 'jmp':
        jmp = process_number_str(instruction_set[i_index][0][1])
        instruction_set[i_index] = 'visited'
        return process_intruction(i_index + jmp, instruction_set, accumulator)
        
def process_number_str(string):

    if string[0] == '+':
        return int(string[1:])
    return int(string)

if __name__ == "__main__":  
    run()