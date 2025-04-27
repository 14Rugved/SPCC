class OperatorPrecedenceParser:
    precedence = {
        '+': {'+': '>', '*': '<', '-': '>', 'a': '<', '$': '>'},
        '*': {'+': '>', '*': '>', '-': '>', 'a': '<', '$': '>'},
        '-': {'+': '<', '*': '<', '-': '>', 'a': '<', '$': '>'},
        'a': {'+': '>', '*': '>', '-': '>', 'a': '>', '$': '>'},
        '$': {'+': '<', '*': '<', '-': '<', 'a': '<', '$': 'A'}
    }

    def __init__(self, expr):
        self.expr = ['$'] + list(expr.replace(" ", "")) + ['$']
        self.stack = ['$']

    def top_terminal(self):
        for sym in reversed(self.stack):
            if sym in self.precedence:
                return sym
        return '$'

    def precedence_of(self, top, next_sym):
        return self.precedence.get(top, {}).get(next_sym, ' ')

    def reduce(self):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == 'a':
                self.stack[i] = 'E'
                return True, "Reduce E → a"
            if i >= 2 and self.stack[i-2] == 'E' and self.stack[i-1] in '+-*' and self.stack[i] == 'E':
                op = self.stack[i-1]
                self.stack[i-2] = 'E'
                del self.stack[i-1:i+1]
                return True, f"Reduce E → E {op} E"
        return False, None

    def is_valid(self):
        prev = ''
        for i, ch in enumerate(self.expr):
            if ch in '+-*' and prev in '+-*':
                return False, i
            prev = ch
        return True, -1

    def parse(self):
        print(f"{'STACK':<20}{'INPUT':<20}{'OUTPUT'}")
        print("=" * 60)

        valid, err_idx = self.is_valid()
        if not valid:
            print(f"{' '.join(self.stack):<20}{' '.join(self.expr[1:-1]):<20}Error: Consecutive Operators")
            print("Not Accepted")
            return

        idx = 1
        while idx < len(self.expr):
            top = self.top_terminal()
            next_sym = self.expr[idx]
            prec = self.precedence_of(top, next_sym)

            if prec in '<=':
                self.stack.append(next_sym)
                print(f"{' '.join(self.stack):<20}{' '.join(self.expr[idx+1:]):<20}Shift {next_sym}")
                idx += 1
            elif prec == '>':
                reduced, action = self.reduce()
                if reduced:
                    print(f"{' '.join(self.stack):<20}{' '.join(self.expr[idx:]):<20}{action}")
                else:
                    print("Error: No valid reduction")
                    return
            elif prec == 'A':
                print(f"{' '.join(self.stack):<20}{' '.join(self.expr[idx:]):<20}Parsing done.")
                print("Accepted")
                return
            else:
                print("Error: Invalid precedence lookup")
                return

        while True:
            reduced, action = self.reduce()
            if reduced:
                print(f"{' '.join(self.stack):<20}{'':<20}{action}")
            else:
                break

        if self.stack == ['$', 'E']:
            print(f"{' '.join(self.stack):<20}{'':<20}Parsing done.")
            print("Accepted")
        else:
            print("Error: Expression not fully reduced.")
            print("Not Accepted")


if __name__ == "__main__":
    expr = input("Enter an arithmetic expression: ")
    parser = OperatorPrecedenceParser(expr)
    parser.parse()
