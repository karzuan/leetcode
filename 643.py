def findMaxAverage(nums, k) -> float:
    n = len(nums)
    if k == 1:
        return max(nums)
    my_list = []
    left, right = 0, k
    for i in range((len(nums) - k) + 1):
        temp = nums[left:right]
        print(temp)
        my_sum = 0
        my_sum += sum(temp)
        my_list.append(my_sum/k)
        left +=1
        right +=1
    print(my_list)
    return(max(my_list))

# def calcAvg

nums = [1,12,-5,-6,50,3]

print(findMaxAverage(nums, 4))
