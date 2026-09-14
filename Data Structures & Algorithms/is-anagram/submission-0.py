class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
                # checking with length of s, t strings
        if len(s) != len(t):
            return False
        # checking with frequency of strings
        s_freq = [0] * 26
        t_freq = [0] * 26
        for ch1,ch2 in zip(s,t):
            # print(f"ch1 - {ch1} = {ord(ch1)-ord('a')}")
            # print(f"ch2 - {ch2} = {ord(ch2)-ord('a')}")
            s_freq[ord(ch1)-ord('a')] += 1
            t_freq[ord(ch2)-ord('a')] += 1
        
        # print('s_freq = ',s_freq)
        # print('t_freq = ',t_freq)
        if s_freq == t_freq:
        
            return True
        else:
            return False