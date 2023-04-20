s = ["h", "e", "l", "l", "o"]
print(s)


def reverseString(s):
    from copy import deepcopy
    cp_s = deepcopy(s[::-1])
    for i in range(len(s)):
        s[i] = cp_s[i]


reverseString(s)
print(s)