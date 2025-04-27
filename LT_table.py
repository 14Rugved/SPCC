def lt_assembler(lines):
    symbol_table = {}
    literal_table = {}
    intermediate_code = []
    location_counter = 0

    # PASS 1
    for line in lines:
        parts = line.strip().split()
        if not parts: continue

        if len(parts) == 3:
            label, opcode, operand = parts
            symbol_table[label] = location_counter
        elif len(parts) == 2:
            opcode, operand = parts
            label = ""
        else:
            opcode = parts[0]
            label = ""
            operand = ""

        if operand.startswith("="):
            literal_table.setdefault(operand, None)

        intermediate_code.append((location_counter, label, opcode, operand))
        location_counter += 1

    # Assign addresses to literals
    for lit in literal_table:
        literal_table[lit] = location_counter
        location_counter += 1

    # PASS 2
    print("\nMachine Code:")
    for loc, label, opcode, operand in intermediate_code:
        address = None
        if operand.startswith("="):
            address = literal_table[operand]
        elif operand in symbol_table:
            address = symbol_table[operand]
        elif operand.isdigit():
            address = operand
        else:
            address = operand  # keep as it is

        print(f"{loc:04d}: {opcode} {address}")

    # Now generate literal pool
    for lit, addr in literal_table.items():
        value = lit.strip("=")
        print(f"{addr:04d}: DC {value}")

    print("\nSymbol Table:", symbol_table)
    print("Literal Table:", literal_table)

# SAMPLE
lt_assembler([
    "START 0",
    "LOAD =5",
    "ADD =10",
    "STORE TEMP",
    "TEMP DS 1",
    "END"
])
