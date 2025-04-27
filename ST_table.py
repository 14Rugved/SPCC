# Simplified ST (Simple Table) Two-Pass Assembler
def st_assembler(lines):
    symbol_table = {}
    location_counter = 0

    # PASS 1
    for line in lines:
        parts = line.strip().split()
        if not parts: continue
        label, opcode, operand = (parts + ["", ""])[:3]
        if opcode == "START":
            location_counter = int(operand)
        if label:
            symbol_table[label] = location_counter
        location_counter += 1

    # PASS 2
    print("\nMachine Code:")
    loc = 0
    for line in lines:
        parts = line.strip().split()
        if not parts: continue
        label, opcode, operand = (parts + ["", ""])[:3]
        address = symbol_table.get(operand, operand)
        print(f"{loc:04d}: {opcode} {address}")
        loc += 1

    print("\nSymbol Table:", symbol_table)


# Sample
st_assembler([
    "START 0",
    "LOAD A",
    "ADD B",
    "STORE C",
    "A DC 5",
    "B DC 3",
    "C DS 1",
    "END"
])
