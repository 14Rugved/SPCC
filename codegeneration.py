import re

def generate_assembly(expression):
    """
    Generate assembly code from a simple arithmetic expression.
    Supports +, -, *, and / operations.
    """
    operators = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}
    assembly_code = []
    temp_counter = 1

    # Tokenize the expression
    tokens = re.findall(r'\d+|[+\-*/()]', expression)
    
    def evaluate_postfix(postfix):
        """
        Generate assembly code for a postfix expression.
        """
        nonlocal temp_counter
        stack = []
        for token in postfix:
            if token.isdigit():  # Operand
                stack.append(token)
            elif token in operators:  # Operator
                operand2 = stack.pop()
                operand1 = stack.pop()
                temp_var = f"T{temp_counter}"
                temp_counter += 1
                assembly_code.append(f"MOV R1, {operand1}")
                assembly_code.append(f"MOV R2, {operand2}")
                assembly_code.append(f"{operators[token]} R1, R2")
                assembly_code.append(f"MOV {temp_var}, R1")
                stack.append(temp_var)
        return stack[0]  # Final result variable

    def infix_to_postfix(tokens):
        """
        Convert infix tokens to postfix notation.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        stack = []
        postfix = []
        for token in tokens:
            if token.isdigit():
                postfix.append(token)
            elif token in operators:
                while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                    postfix.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove '('
        while stack:
            postfix.append(stack.pop())
        return postfix

    # Convert infix to postfix and generate assembly code
    postfix = infix_to_postfix(tokens)
    final_result = evaluate_postfix(postfix)
    assembly_code.append(f"; Final result stored in {final_result}")
    assembly_code.append(f"PRINT {final_result}  ; Output the final result")

    return '\n'.join(assembly_code)

# Example usage
python_expression = input("Enter a Python arithmetic expression: ")
assembly_output = generate_assembly(python_expression)
print("\n### Generated Assembly Code ###")
print(assembly_output)

