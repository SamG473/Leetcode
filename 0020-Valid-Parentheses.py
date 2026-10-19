class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for elem in s:
            if elem in "([{":                 # opener, so push it
                stack.append(elem)
            else:                             # closer, so check it
                if not stack or stack[-1] != pairs[elem]:
                    return False              # nothing to match, or wrong opener
                stack.pop()                   # matched, so remove the opener

        return not stack                      # valid only if nothing is left over
