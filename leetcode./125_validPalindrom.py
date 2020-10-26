class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        l_idx = 0
        r_idx = len(s) - 1
        while l_idx <= r_idx:
            if s[l_idx].isalnum() != True:
                l_idx += 1
            if s[r_idx].isalnum() != True:
                r_idx -= 1
            if s[l_idx].isalnum() and s[r_idx].isalnum():
                if s[l_idx] != s[r_idx]:
                    return False
                else:
                    l_idx += 1
                    r_idx -= 1
        return True
