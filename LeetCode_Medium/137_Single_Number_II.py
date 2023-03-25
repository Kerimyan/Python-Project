nums = [4,2,4,4,5,2,6,6,6,8,5,3,2,2,4,3,9,9]
inx = 0
while len(nums) != 1:
    num_1 = nums.pop(inx)
    if num_1 in nums:
        while num_1 in nums:
            nums.remove(num_1)
    else:
        resunt = num_1
        break
if len(nums) == 1:
    resunt = int(nums[0])
print(resunt)