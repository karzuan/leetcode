def maxOperations(nums, k: int):
    left, right = 0, (len(nums) - 1)
    nums.sort()
    result = 0
    while left < right:
        sum = nums[left] + nums[right]
        print(sum, nums[left], nums[right])
        if sum == k:
            result += 1
            left += 1
            right -= 1
        elif sum > k:
            right -= 1
        else:
            left += 1

    return result

# [3,1,3,4,3], k=6
#[1,2,3,4], k=5
# [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], k = 2
# sorted: [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]
nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
maxOperations(nums, 2)