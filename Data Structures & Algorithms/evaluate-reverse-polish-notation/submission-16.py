class Solution:
        def evalRPN(self, tokens: List[str]) -> int:
            stack = []
            for token in tokens:
                if token in ["+", "-", "*", "/"]:
                    val2 = stack.pop()
                    val1 = stack.pop()
                    if token == "+":
                        tot = val1 + val2
                        stack.append(tot)
                    elif token == "-":
                        tot = val1 - val2
                        stack.append(tot)
                    elif token == "*":
                        tot = val1 * val2
                        stack.append(tot)
                    elif token == "/":
                        tot = int(val1 / val2)
                        stack.append(tot)
                else:
                    stack.append(int(token))
            return stack.pop()
