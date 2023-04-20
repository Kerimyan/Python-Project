# s = "()"         #Output: true

# s = "()[]{}"     #Output: true

# s = "(]"         #Output: false

# s = "{[]}"       #Output: true

# s = "([)]"        #Output: false

# s= ']'             #Output: false

s= "[([]])"          #Output: false



def isValid(s: str):
    seen = []
    for bracket in s:
        if bracket in ('(', '[', '{'):
            seen.append(bracket)
            continue
        if bracket == ')' and '(' in seen and '(' == seen[-1]:
            seen.pop(-1)
            continue
        elif bracket == ']' and '[' in seen and '[' == seen[-1]:
            seen.pop(-1)
            continue
        elif bracket == '}' and '{' in seen and  '{' == seen[-1]:
            seen.pop(-1)
            continue
        else:
            return False
    else:
        if seen == []:
            return True
        else:
            return False



print(isValid(s))
