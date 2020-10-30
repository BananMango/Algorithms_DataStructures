class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}
        
        for i in range(len(s)):
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]
        
        str_s_new = ''.join([t_map[T] for T in t])
        str_t_new = ''.join([s_map[S] for S in s])
        return str_s_new == s and str_t_new == t
