class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # two-pointer approach
        l,r = 0,n-1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum < target:
                l+=1
            elif current_sum > target:
                r-=1
            elif current_sum == target:
                return [l+1,r+1]