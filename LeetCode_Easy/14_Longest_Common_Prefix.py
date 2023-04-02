strs = ["aca","cba"]

shortest = min(strs, key=len)

def letter_check(list, subinx):
    letter = list[0][subinx]
    res = ''
    for i in range(len(list)):
        if letter == list[i][subinx]:
            res += letter
    if len(res) != len(list):
        return None
    else:
        return res[0]

result = ''
for i in range(len(shortest)):
    x = letter_check(strs, i)
    if x == None:
        break
    else:
        result += x
print(result)