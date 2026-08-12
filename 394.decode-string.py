class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num = 0
        current_string = ''
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_string, current_num))
                current_string = ''
                current_num = 0
            elif char == ']':
                last_string, num = stack.pop()
                current_string = last_string + current_string * num
            else:
                current_string += char
        
        return current_string
a = Solution()
print(a.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(a.decodeString("3[a2[c]]"))  # Output: "accaccacc"