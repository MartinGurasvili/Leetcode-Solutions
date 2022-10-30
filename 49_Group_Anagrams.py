class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp=[]
        ff = []
        for x in strs:
            hs = hash(str(sorted(x)))
            if hs in ff:
                temp[ff.index(hs)].append(x)
            else:
                temp.append([x])
                ff.append(hs)
        return temp
