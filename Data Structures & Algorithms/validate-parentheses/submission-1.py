class Solution:
    def isValid(self, s: str) -> bool:
                # closing_brakcet -> opening_bracket # key -> value
        dict1 = {')':'(',']':'[','}':'{'}
        stack = []
        for ch in s:
            # validate opening brackets
            if ch in dict1.values():
                stack.append(ch)
            if ch in dict1.keys():
                if len(stack)==0:
                    return False
                top_elem = stack[-1] # peek
                if dict1[ch] == top_elem:
                    stack.pop()
                else:
                    return False
        return len(stack)==0