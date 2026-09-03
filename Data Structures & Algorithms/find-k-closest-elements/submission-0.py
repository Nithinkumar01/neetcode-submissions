class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = sorted(arr, key=lambda num: abs(num - x))
        return sorted(result[:k])