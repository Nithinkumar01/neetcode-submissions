class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            current = 0
            days_needed = 1

            for weight in weights:
                if current + weight > mid:
                    days_needed += 1
                    current = 0

                current += weight

            if days_needed <= days:
                right = mid
            else:
                left = mid + 1

        return left