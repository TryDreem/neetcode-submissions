class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for ele in strs:
            s_ele = "".join(sorted(ele))
            if s_ele not in anagrams:
                anagrams[s_ele] = [ele]
            else:
                anagrams[s_ele].append(ele)
        
        return [a for a in anagrams.values()]