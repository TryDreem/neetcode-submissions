class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        elements_s = Counter(s)
        for ele in t:
            if ele in elements_s and elements_s[ele] >= 1:
                elements_s[ele] -= 1
            else:
                return False
        return sum(elements_s.values()) == 0 
