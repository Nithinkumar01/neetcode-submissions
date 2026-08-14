from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        freq = {}

        # Count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        print(freq[num])
        # Collect answers
        result = []

        for num, count in freq.items():
            if count > target:
                result.append(num)

        return result