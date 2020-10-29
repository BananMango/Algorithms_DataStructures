class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        
        word_len = len(words[0])
        total_words_len = len(words) * word_len
        
        if len(s) < total_words_len or len(s) == 0:
            return []
        
        words_counter = Counter(words)
        res = []
        i = 0
        
        while i <= len(s) - total_words_len:
            substring = s[i : i + total_words_len]
            substring_arr = [substring[a : a + word_len] for a in range(0, total_words_len, word_len)]
            substring_counter = Counter(substring_arr)
            if substring_counter == words_counter:
                res.append(i)
            i += 1
        return res
