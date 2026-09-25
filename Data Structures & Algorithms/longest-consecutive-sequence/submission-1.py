class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        long_seq = []
        for num in nums_set:
            if num-1 not in nums_set:
                temp_seq = [num]
                check_num = num
                while check_num + 1 in nums_set:
                    check_num = check_num+1
                    temp_seq.append(check_num)
                if len(temp_seq) > len(long_seq):
                    long_seq = temp_seq
        return len(long_seq)