class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for ele in strs:
            r = "".join(sorted(ele))
            res[r].append(ele)

        return [i for i in res.values()]
                