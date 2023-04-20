# nums1 = [5,8,2,7]
# nums2 = [5,2,8,4,7,1,3]
#
nums1 = [7,5,6]
nums2 = [1,4]

def minNumber(nums1, nums2):
    x = list(set(nums1) & set(nums2))
    if x != []:
        return min(x)
    else:
        a = str(min(nums1))
        b = str(min(nums2))
        res = min(a,b) + max(a,b)
        return int(res)

print(minNumber(nums1, nums2))