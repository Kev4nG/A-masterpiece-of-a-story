import random

numberList = [random.randint(1, 50) for _ in range(10)]
def sortList(nums):
    for j in range(len(nums)):
        for i in range(len(nums)-1):
            back = nums[i]
            front = nums[i + 1]
            if front < back:
                front ^= back
                back ^= front
                front ^= back
                
                nums[i] = back
                nums[i + 1] = front
                
    return nums
                
print(sortList(numberList))