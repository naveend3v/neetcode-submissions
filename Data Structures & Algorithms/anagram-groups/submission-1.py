class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        size_of_strs = len(strs)
    
        freq_map = {}

        for word in strs:        
            freq1 = [0]*26
            for i in range(len(word)):
                freq1[ord(word[i]) - ord('a')]+=1
            if str(freq1) in freq_map:
                freq_map[str(freq1)].append(word)
            else:
                freq_map[str(freq1)] = [word]
        
        return list(freq_map.values())