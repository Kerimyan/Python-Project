s = "abc"
t = "ahbgdc"

# s = "axc"
# t = "ahbgdc"
#
# s = "ab"
# t = "baab"
#
def isSubsequence(s, t):
    s_list = list(s)
    for i in t:
        if s_list and s_list[0] == i:
            s_list.pop(0)

    if s_list == []:
        return True
    else:
        return False


    # n_s = ''
    # for i in t:
    #     if i in s:
    #         n_s += i
    # if s in n_s:
    #     return True
    # else:
    #     return False
    #
    #

print(isSubsequence(s,t))