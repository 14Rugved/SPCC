# Simplified BT (Base Table) Two-Pass Assembler
def bt_assembler(lines):
    symbol_table = {}
    base_table = {}
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
        if opcode == "USING":
            base_table[operand.split(',')[0]] = location_counter
        location_counter += 4

    # PASS 2
    print("\nMachine Code:")
    loc = 0
    for line in lines:
        parts = line.strip().split()
        if not parts: continue
        label, opcode, operand = (parts + ["", ""])[:3]
        print(f"{loc:04d}: {opcode} {operand}")
        loc += 4

    print("\nSymbol Table:", symbol_table)
    print("Base Table:", base_table)


# Sample
bt_assembler([
    "COPY START 0",
    "FIRST USING *,15",
    "L 1,FOUR",
    "A 1,FIVE",
    "ST 1,TEMP",
    "FOUR DC F'4'",
    "FIVE DC F'5'",
    "TEMP DS 1F",
    "END"
])
