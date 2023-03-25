nums = [4, 2, 1, 5, 5, 7, 4, 1, 2, 7, 8]
inx = 0
while len(nums) != 1:
    num_1 = nums.pop(inx)
    if num_1 in nums:
        nums.remove(num_1)
    else:
        resunt = num_1
        break
if len(nums) == 1:
    resunt = int(nums[0])
print(resunt)
