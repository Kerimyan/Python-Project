n = 19
lim = 0
while True:
     lim += 1
     res = 0
     for i in str(n):
          res += int(i)**2
          n = res
     if n == 1:
          output = True
          break
     elif lim == 50:
          output = False
          break


print(output)
