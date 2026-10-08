class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        elements_s = dict(Counter(s))
        for ele in t:
            if ele in elements_s and elements_s[ele] >= 1:
                elements_s[ele] -= 1
            else:
                return False
        return True if sum(elements_s.values()) == 0 else False
