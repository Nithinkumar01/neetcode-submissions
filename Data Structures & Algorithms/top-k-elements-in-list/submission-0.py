class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequency
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Sort by frequency descending
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Take first k elements
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result