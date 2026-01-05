class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            s_s = ''.join(sorted(s))
            d[s_s].append(s)

        res =  d.values()
        return list(res)