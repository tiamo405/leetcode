class Solution(object):
    def caculate(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return int(float(a) / b)
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.caculate(b, a, token))
                print(stack[-1])
            else:
                stack.append(int(token))
        return int(stack[0])
a = Solution()
print(a.evalRPN(["2","1","+","3","*"])) # 9
print(a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))