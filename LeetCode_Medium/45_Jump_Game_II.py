nums = [2,3,0,1,4]

def jump(nums):
    jump_count = 0
    point_ind = 0
    jump_max = 0
    for i, num in enumerate(nums[:-1]):
        jump_max = max(i + num, jump_max)
        if i == point_ind:
            point_ind = jump_max
            jump_count += 1
    return jump_count




print(jump(nums))