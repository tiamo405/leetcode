class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []
        for i in path:
            if i != '' and i != '.':
                stack.append(i)
        new_stack = []
        for i in range(len(stack)-1):
            new_stack.append(stack[i])
            if stack[i+1] == "..":
                if len(new_stack) > 0:
                    new_stack.pop()
            if stack[i] == '..':
                if len(new_stack) > 0:
                    new_stack.pop()
        if len(stack) > 0 and stack[-1] != "..":
            new_stack.append(stack[-1])
        new_stack = "/".join(new_stack)
        return '/'+new_stack
       
    
a = Solution()
print(a.simplifyPath("/"))
print(a.simplifyPath("/a/../../b/../c//.//"))
print(a.simplifyPath("/.../a///../b/c//..//d/./"))
print(a.simplifyPath("/home//fod"))
print(a.simplifyPath("/../"))
