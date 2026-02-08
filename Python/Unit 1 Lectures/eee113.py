def convert_to_twos_complement(value, num_bits):
    return bin((1 << num_bits) + value if value < 0 else value)[2:].zfill(num_bits)

def parse_instruction(instruction):
    register_mapping = {'R0': '00', 'R1': '01', 'R2': '10', 'R3': '11'} # Register assignment for mux/demux selectors
    operation_mapping = {'ADD': '00', 'SUB': '01', 'AND': '10', 'OR': '11'} # Operation assignment
    condition_mapping = {'EQ': '00', 'NE': '01', 'LT': '10', 'GT': '11'} # Branch condition check for PC mux selector
    
    parts = instruction.split()
    write_en = str(int(not parts[0].startswith('B'))) # Always write unless it is a branch
    operation = condition_mapping[parts[0].lstrip('B')] if parts[0].startswith('B') else operation_mapping[parts[0].rstrip('I')] # Extract the operation bits
    const_sel = str(int(not (parts[0].endswith('I') or parts[0].startswith('B')))) # Everything that ends with I is an immediate
    destreg = '00' if parts[0].startswith('B') else register_mapping[parts[1].rstrip(',')] # This is a don't care if it is a branch instruction actually
    
    # If instruction is branch, the source register is the register at index 1 (destreg), else it is at index 2 (since dest register would be at index 1)
    srcreg = register_mapping[parts[1].rstrip(',')] if parts[0].startswith('B') else register_mapping[parts[2].rstrip(',')] 
    
    if parts[0].endswith('I'):  # If the instruction is an immediate type, convert to two's complement notation
        const = convert_to_twos_complement(int(parts[3].rstrip(',')), 8)
    elif parts[0].startswith('B'): # Branch instructions have their constants on index 2 instead of 3
        const = convert_to_twos_complement(int(parts[2].rstrip(',')), 8)
    else: # If the instruction does not have a constant, then it is a purely register-based instruction
        const = '000000' + register_mapping[parts[3].rstrip(',')]

    binary_result = write_en + operation + const_sel + destreg + srcreg + const # Combine all binary into 16-bit instruction
    hex_result = hex(int(binary_result, 2))[2:].zfill(4).upper() # convert to hex
    return hex_result
# End of actual assembler function. Less than 30 lines!

# Supported instructions:
    # ADD R1, R2, R3    R1 = R2 + R3
    # ADDI R1, R2, 5    R1 = R2 + 5 (constant [-128, 127])
    # SUB R1, R2, R3    R1 = R2 - R3
    # SUBI R1, R2, 5    R1 = R2 - 5 (constant [-128, 127])
    # AND R1, R2, R3    R1 = R2 & R3 (bitwise)
    # ANDI R1, R2, 5    R1 = R2 & 5 (bitwise against a constant [-128, 127])
    # OR R1, R2, R3     R1 = R2 | R3 (bitwise)
    # ORI R1, R2, 5     R1 = R2 | 5 (bitwise against a constant [-128, 127])
    # BEQ R0, -4        If R0 = 0, jump to -4 (constant [-128, 127]) instructions from the current instruction
    # BNE R0, -4        If R0 != 0, jump to -4 (constant [-128, 127]) instructions from the current instruction
    # BLT R0, -4        If R0 < 0, jump to -4 (constant [-128, 127]) instructions from the current instruction
    # BGT R0, -4        If R0 > 0, jump to -4 (constant [-128, 127]) instructions from the current instruction
    
# Some example assembly code to test the processor
instructions_test1 = [  # This is the sample code used in the lecture. Just plain arithmetic instructions.
    "ADDI R3, R0, 113",   # R3 = R0 + 113 = 0 + 113 = 113
    "ADDI R2, R2, 21",    # R2 = R2 + 21 = 0 + 21 = 21
    "SUB R1, R3, R2",     # R1 = R3 - R2 = 113 - 21 = 92
    "ANDI R1, R1, 15",    # R1 = R1 & 15 = 92 (0101 1100) & 15 (0000 1111) = 12 (0000 1100)
    "OR R0, R2, R1"       # R0 = R2 | R1 = 21 (0001 0101) | 12 (0000 1100) = 29 (0001 1101)
]

instructions_test2 = [  # This is the sample code used in the lecture to demonstrate a branch instruction.
    "ADDI R2, R2, 5",   # R2 = R2 + 5 = 0 + 5 = 5
    "ADDI R1, R1, 1",   # R1 = R1 + 1
    "SUBI R2, R2, 1",   # R2 = R2 - 1
    "BNE R2, -2"        # As long as R2 != 0, loop two steps backward (back to ADDI R1, R1, 1)
]

# Pick the instructions to assemble into hexcode
instructions = instructions_test1
#instructions = ["SUBI R3, R1, -31"] # The 0xADE1 instruction :)
hex_results = [parse_instruction(instruction) for instruction in instructions]

with open('instructions', 'w') as file:
    print('v2.0 raw',file=file) # header for Logisim memory
    print(' '.join(hex_results), file=file)
    print(' '.join(hex_results))