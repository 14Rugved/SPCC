import re

def get_temp():

    global temp_count
    temp = f"T{temp_count}"
    temp_count += 1
    return temp

def infix_to_postfix(tokens):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    output, stack = [], []

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output

def postfix_to_TAC(postfix):
    tac_code, stack = [], []

    for token in postfix:
        if token.isdigit():
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            temp = get_temp()
            tac_code.append(f"{temp} = {a} {token} {b}")
            stack.append(temp)
    return tac_code

# Main program
temp_count = 1
expr = input("Enter an arithmetic expression: ")
tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expr)
postfix = infix_to_postfix(tokens)
tac = postfix_to_TAC(postfix)

print("\nGenerated Three-Address Code:")
for line in tac:
    print(line)
