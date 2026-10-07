class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_str = "".join(char.lower() for char in s if char.isalnum())
        # print(f"filter str = {filter_str}")
        rev_str = filter_str[::-1]
        # print(f"rev str = {rev_str}")
        if (filter_str == rev_str):
            return True
        return False