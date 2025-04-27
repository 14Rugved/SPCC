# Input
n = int(input("Enter the number of expressions: "))
print("Enter the expressions in the format 'left = right':")

expressions = [{"left": input("Left: ").strip(), "right": input("Right: ").strip()} for _ in range(n)]

# Intermediate Code
print("\nIntermediate Code:")
for expr in expressions:
    print(f"{expr['left']} = {expr['right']}")

# Step 1: Identify Constants
constants = {}
optimized_exprs = []

for expr in expressions:
    right = expr["right"]
    # If right side is a constant number
    if right.isdigit():
        constants[expr["left"]] = right
    else:
        # Replace variables in right side with constants if available
        parts = right.split()
        new_right = []
        for part in parts:
            new_right.append(constants.get(part, part))
        expr["right"] = ' '.join(new_right)

    optimized_exprs.append(expr)

# After Constant Propagation
print("\nAfter Constant Propagation:")
for expr in optimized_exprs:
    print(f"{expr['left']} = {expr['right']}")

# Step 2: Dead Code Elimination (optional to match your structure)
used_vars = {expr["left"] for expr in optimized_exprs if any(expr["left"] in other["right"] for other in optimized_exprs)}
final_exprs = [expr for i, expr in enumerate(optimized_exprs) if expr["left"] in used_vars or i == len(optimized_exprs) - 1]

print("\nAfter Dead Code Elimination:")
for expr in final_exprs:
    print(f"{expr['left']} = {expr['right']}")

# Step 3: Final Duplicate Removal
seen = set()
optimized_final = []

for expr in final_exprs:
    key = (expr["left"], expr["right"])
    if key not in seen:
        seen.add(key)
        optimized_final.append(expr)

# Optimized Code
print("\nOptimized Code:")
for expr in optimized_final:
    print(f"{expr['left']} = {expr['right']}")
