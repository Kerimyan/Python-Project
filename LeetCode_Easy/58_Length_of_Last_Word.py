s = input("input a string!! ")

words = s.split(" ")
inx = 1
lst = words[-inx]
while lst == '':
    inx += 1
    lst = words[-inx]

print(len(lst))
