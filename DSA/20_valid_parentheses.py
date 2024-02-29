#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for element in s:
            if element in '([{':
                stack.append(element)
            else:
                if len(stack) == 0 or \
                    (element == ')' and stack[-1] != '(') or \
                    (element == ']' and stack[-1] != '[') or \
                    (element == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return len(stack) == 0