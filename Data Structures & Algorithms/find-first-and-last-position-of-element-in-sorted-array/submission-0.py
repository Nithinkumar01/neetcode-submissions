class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        if len(result) == 0:
            return [-1, -1]

        return [result[0], result[-1]]