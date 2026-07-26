class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Remove counts using characters from t
        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1

            # More characters in t than s
            if count[ch] < 0:
                return False

        return True