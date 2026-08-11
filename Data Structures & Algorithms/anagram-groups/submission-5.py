class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        res = []
        for string in strs:
            sort = str(sorted(string))
            if sort not in hmap.keys():
                hmap[sort] = []
            hmap[sort] += [string]
        for key in hmap:
            res.append(hmap[key])
        return res
        