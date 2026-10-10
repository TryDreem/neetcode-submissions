class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            best = max(best, right - left + 1)

        return best