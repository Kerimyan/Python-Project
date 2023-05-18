# digits = "23"

# digits = ""
#
# digits = "2"

digits = "234"

#
# def letterCombinations(digits: str):
#     d = {'2': ['a', 'b', 'c'],
#          '3': ['d', 'e', 'f'],
#          '4': ['g', 'h', 'i'],
#          '5': ['j', 'k', 'l'],
#          '6': ['m', 'n', 'o'],
#          '7': ['p', 'q', 'r', 's'],
#          '8': ['t', 'u', 'v'],
#          '9': ['w', 'x', 'y', 'z']}
#     if digits == '':
#         return []
#     elif len(digits) == 1:
#         return d[digits]
#     lst = []
#     for v in d.values():
#         lst.append(v)
#

def letterCombinations(digits: str):
    if not digits:
        return []
    digit_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
    }
    result = []
    def backtrack(index, combination):
        if index == len(digits):
            result.append(combination)
            return
        for letter in digit_map[digits[index]]:
            backtrack(index + 1, combination + letter)
            combination = combination[:]
    backtrack(0, "")
    return result




print(letterCombinations(digits))