class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap={} # tuple[int] : [list]
        for str in strs:
            freq=[0]*26
            for i,n in enumerate(str):
                freq[ord(n)-ord('a')] += 1
            if tuple(freq) in prevMap:
                prevMap[tuple(freq)].append(str)
            else:
                prevMap[tuple(freq)] = [str]
        # print(json.dumps(prevMap,indent=4))
        return list(prevMap.values())