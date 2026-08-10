class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxFreq = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            # highest frequency in current window
            maxFreq = max(maxFreq, count[s[right]])

            # if replacements needed > k, shrink window
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans