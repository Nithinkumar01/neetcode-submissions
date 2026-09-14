class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        have = 0
        need_count = len(need)

        best_length = float("inf")
        best_left = 0
        best_right = 0

        for right in range(len(s)):

            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:

                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                left_ch = s[left]

                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_right + 1]