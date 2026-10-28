class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        Hmap = {}
        l = 0
        for r in range(len(s)):
            Hmap[s[r]] = 1 + Hmap.get(s[r], 0)
            while r - l + 1  - max(Hmap.values()) > k:
                Hmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
