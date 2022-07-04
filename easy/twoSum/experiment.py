import re

def twoSum(nums, target: int):
    for i in range(0, len(nums)) :
        for j in range(i + 1, len(nums)) :
            if (nums[i] + nums[j] == target) :
                return [i, j]

strings = input()
target = int(input())

nums = re.compile(r"\d+").findall(strings)
for i in range(len(nums)):
    nums[i] = int(nums[i])

print(twoSum(nums, target))
