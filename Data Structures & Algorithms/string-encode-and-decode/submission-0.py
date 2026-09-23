class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for str1 in strs:
            final = final + str(len(str1)) + '#' + str1
        return final
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j = j+1
            str_len = int(s[i:j])
            start_idx = j + 1
            end_idx = start_idx + str_len
            word = s[start_idx:end_idx]
            res.append(word)
            i=end_idx
        return res

