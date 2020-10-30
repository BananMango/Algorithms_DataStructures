class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for ch in s:
            if ch in hashmap.keys():
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1
        
        for i in range(len(s)):
            if hashmap[s[i]] < 2:
                return i
        return -1
