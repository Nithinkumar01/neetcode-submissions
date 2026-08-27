class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_max = [0] * n
        right_max = [0] * n

        # Find maximum height from the left
        left_max[0] = height[0]

        for i in range(1, n):
            if height[i] > left_max[i - 1]:
                left_max[i] = height[i]
            else:
                left_max[i] = left_max[i - 1]

        # Find maximum height from the right
        right_max[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            if height[i] > right_max[i + 1]:
                right_max[i] = height[i]
            else:
                right_max[i] = right_max[i + 1]

        total = 0

        # Calculate water
        for i in range(n):
            if left_max[i] < right_max[i]:
                total += left_max[i] - height[i]
            else:
                total += right_max[i] - height[i]

        return total