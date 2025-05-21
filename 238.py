def productExceptSelf(nums):
    result = len(nums) * [1]
    temp = [ [] for i in range(len(nums))]
    for i in range(len(nums)):
        for k in range(len(nums)):
            if k != i:
                temp[i].append(nums[k])
    for i in range(len(nums)):
        for k in temp[i]:
            result[i] *= k
    return result

print(productExceptSelf([1, 2, 3, 4]))