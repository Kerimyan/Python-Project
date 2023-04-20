s = "abcd"
t = "abcde"

# s = ""
# t = "y"

# s = "a"
# t = "aa"


def findTheDifference(s, t):
    l = list(t)
    for i in s:
        if i in l:
            l.remove(i)
    return l[0]


print(findTheDifference(s, t))
