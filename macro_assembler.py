# Initialize the MNT and MDT tables
def initialize_tables():
    mnt = []  # Macro Name Table (MNT)
    mdt = []  # Macro Definition Table (MDT)
    return mnt, mdt

# Display MNT and MDT
def display_tables(mnt, mdt, pass_num, stage=""):
    print(f"\n--- Pass {pass_num} {stage} ---")
    print("\nMNT (Macro Name Table):")
    for entry in mnt:
        print(entry)

    print("\nMDT (Macro Definition Table):")
    for entry in mdt:
        print(entry)

# Process the macro from input assembly code
def process_macro(input_file):
    mnt, mdt = initialize_tables()  # Initialize MNT and MDT
    pass1_output = []
    pass2_output = []
    
    with open(input_file, 'r') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # If it's a macro definition
        if line.upper() == "MACRO":
            i += 1
            macro_def = lines[i].strip().split()
            macro_name = macro_def[0]
            parameters = macro_def[1:] if len(macro_def) > 1 else []
            mnt.append((macro_name, len(mdt)))  # Insert macro name with its MDT index

            i += 1
            macro_body = []
            while i < len(lines) and lines[i].strip().upper() != "MEND":
                current_line = lines[i].strip()
                # Replace parameters with #index in the macro body
                for param in parameters:
                    current_line = current_line.replace(param, "#" + str(parameters.index(param)))
                macro_body.append(current_line)
                i += 1

            mdt.append(macro_body)  # Insert macro body into MDT
            mdt.append(["MEND"])  # MEND marks the end of the macro

            display_tables(mnt, mdt, 1, f"After defining {macro_name}")
        else:
            pass1_output.append(line)  # Regular assembly code for Pass 1
            i += 1

    print("\n##### Pass 1 Output #####")
    for idx, line in enumerate(pass1_output, 1):
        print(f"{idx}\t{line}")
    
    # Pass 2: Expand macros in the assembly code
    print("\n##### Pass 2 Output #####")
    for line in pass1_output:
        parts = line.split()
        if parts[0] in [macro[0] for macro in mnt]:  # If macro is called
            macro_name = parts[0]
            args = parts[1:] if len(parts) > 1 else []
            
            # Find the macro definition in MDT using MNT
            for macro in mnt:
                if macro[0] == macro_name:
                    mdt_index = macro[1]
                    break
            
            macro_body = mdt[mdt_index]
            for definition in macro_body:
                expanded_line = definition
                for i in range(len(expanded_line.split())):
                    if expanded_line.split()[i].startswith("#"):
                        arg_index = int(expanded_line.split()[i][1:])
                        if arg_index < len(args):
                            expanded_line = expanded_line.replace(expanded_line.split()[i], args[arg_index])
                pass2_output.append(expanded_line)
        else:
            pass2_output.append(line)
    
    # Output the final expanded code after Pass 2
    print("\n##### Final Pass 2 Output #####")
    for idx, line in enumerate(pass2_output, 1):
        print(f"{idx}\t{line}")

# Main function to drive the process
def main():
    input_file = "input.txt"
    process_macro(input_file)

if __name__ == "__main__":
    main()
