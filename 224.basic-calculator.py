class Solution(object):
    def calculate_simple(self, s): # hàm xử lý biểu thức đơn giản chỉ có + -
        """
        :type s: str
        :rtype: int
        """
        stack = []
        current_number = 0
        operation = '+'
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            if char in "+-" or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                operation = char
                current_number = 0
        return sum(stack)
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # remove spaces
        s = s.replace(" ", "")
        # kieẻm tra ngoặc, nếu là ( + - số thì put vao stack (nếu là ( thì lưu vị trí vào 1 mảng khác) ) . nếu ) thì bắt đầu xử lý như sau: lấy string từ vị trsi cuối cùng của ( và vị trí hiện tại, xử lý biểu thức bên trong ngoặc bằng hàm calculate_simple, sau đó thay thế biểu thức trong ngoặc bằng kết quả đã tính được
        stack = []
        open_paren_indices = []
        i = 0
        while i < len(s):
            char = s[i]
            if char == '(':
                open_paren_indices.append(len(stack))
                stack.append(char)
            elif char == ')':
                last_open_index = open_paren_indices.pop()
                expr = ''.join(stack[last_open_index + 1:])
                stack = stack[:last_open_index]
                result = self.calculate_simple(expr)
                # kiểm tra nếu kết quả là số âm và trước đó là dấu + hoặc - thì thêm dấu vào stack
                if result < 0 :
                    if stack and stack[-1] in '+-':
                        sign = stack.pop()
                        if sign == '+':
                            stack.append('-')
                        else:
                            stack.append('+')
                    else:
                        stack.append('-')
                    result = -result
                for c in str(result):
                    stack.append(c)
            else:
                stack.append(char)
            i += 1
        final_expr = ''.join(stack)
        return self.calculate_simple(final_expr)
                
a = Solution()
print(a.calculate("1-(-2)"))  # 3
print(a.calculate_simple("-3-2")) 
print(a.calculate("1 + 1"))  # 2
print(a.calculate(" 2-1 + 2 "))  # 3
print(a.calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
print(a.calculate("- (3 + (4 + 5))"))  # -12