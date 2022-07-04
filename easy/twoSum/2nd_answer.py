class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            if num not in d:
                d[num] = [index]
            else:
                d[num].append(index)
        for num in nums:
            t = target - num
            if t in d and t == num and len(d[num]) > 1:
                return [d[num][0], d[num][1]]
            if t != num and t in d:
                return [d[num][0], d[t][0]]
