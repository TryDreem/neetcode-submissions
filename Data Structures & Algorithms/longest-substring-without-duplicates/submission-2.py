class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        left = 0
        for r in range(left, len(s)):   # sysyf
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[r])
            best = max(best, len(seen))
        return best
