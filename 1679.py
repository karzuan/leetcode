

def maxOperations(nums, k: int):
    result = 0
    flag = True
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                a, b = nums[i], nums[j]
                result += checkSum(a, b, k)

    print(result)


def run


def checkSum(i, j, k):
    if (i + j) == k:
        print(f"{i} + {j} = ", k)
        return 1
    else: return 0


nums = [3,1,3,4,3]
maxOperations(nums, 6)