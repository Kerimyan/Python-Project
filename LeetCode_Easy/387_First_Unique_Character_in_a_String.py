# s = "leetcode"

# s = "loveleetcode"
#
s = "aabb"


# version 1
# def firstUniqChar(s: str):
#     for i in s:
#         if s.count(i) == 1:
#             return s.index(i)
#     else:
#         return -1
#
# print(firstUniqChar(s))


def firstUniqChar(s: str):
    t_dict = {}
    for i in s:
        if i not in t_dict:
            t_dict[i] = 1
        else:
            t_dict[i] += 1

    for i in s:
        if t_dict[i] == 1:
            return s.index(i)
    else:
        return -1


print(firstUniqChar(s))