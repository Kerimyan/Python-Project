words = ["Hello","Alaska","Dad","Peace"]    #Output: ["Alaska","Dad"]

# words = ["omk"]                            # Output: []
#
# words = ["adsdf","sfd"]                    # Output: ["adsdf","sfd"]


def findWords(words):
    res = []
    l1 = "qwertyuiop"
    l2 = "asdfghjkl"
    l3 = "zxcvbnm"
    for i in words:
        temp1 = ''
        temp2 = ''
        temp3 = ''
        for j in range(len(i)):
            if i[j].lower() in l1:
                temp1+=i[j]
            elif i[j].lower() in l2:
                temp2+=i[j]
            elif i[j].lower() in l3:
                temp3+=i[j]
        else:
            if temp1 == i or temp2 == i or temp3 == i:
                res.append(i)
    return res



print(findWords(words))