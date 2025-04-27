# Input
n = int(input("Enter the number of expressions: "))
print("Enter the expressions in the format 'left = right':")

expressions = [{"left": input("Left: ").strip(), "right": input("Right: ").strip()} for _ in range(n)]

# Intermediate Code
print("\nIntermediate Code:")
for expr in expressions:
    print(f"{expr['left']} = {expr['right']}")

# Step 1: Dead Code Elimination
used_vars = {expr["left"] for expr in expressions if any(expr["left"] in other["right"] for other in expressions)}
optimized_exprs = [expr for i, expr in enumerate(expressions) if expr["left"] in used_vars or i == len(expressions) - 1]

print("\nAfter Dead Code Elimination:")
for expr in optimized_exprs:
    print(f"{expr['left']} = {expr['right']}")

# Step 2: Common Subexpression Elimination
subexp_map = {}
final_exprs = []

for expr in optimized_exprs:
    if expr["right"] in subexp_map:
        replacement = subexp_map[expr["right"]]
        for e in optimized_exprs:
            e["right"] = e["right"].replace(expr["left"], replacement)
    else:
        subexp_map[expr["right"]] = expr["left"]
        final_exprs.append(expr)

print("\nAfter Eliminating Common Expressions:")
for expr in final_exprs:
    print(f"{expr['left']} = {expr['right']}")

# Step 3: Final Optimization (Duplicate Removal)
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
