def run():
    with open('input.txt') as f:
        instruction_set = [(i.split(), False) for i in f.read().split('\n')]
        print(f'Answer: {process_intruction(0, instruction_set, 0)}')


def process_intruction(i_index, instruction_set, accumulator):
    # If we have seen the instruction before it is time to exit the loop
    if instruction_set[i_index] == 'visited':
        return accumulator
    
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