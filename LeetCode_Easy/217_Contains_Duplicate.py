nums = [1,2,3,4,5,6,5]
temp = set()
res = False
for i in nums:
    if i in temp:
        res = True
        break
    temp.add(i)
print(res)