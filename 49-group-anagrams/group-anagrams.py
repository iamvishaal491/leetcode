class Solution(object):
    def groupAnagrams(self, strs):
        group=defaultdict(list)
        result=[]
        for i in strs:
            sorted_i=tuple(sorted(i))
            group[sorted_i].append(i)
        for i in group.values():
            result.append(i)
        return result 