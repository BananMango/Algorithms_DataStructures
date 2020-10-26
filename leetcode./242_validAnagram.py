class Solution:
    def construct_dict(self, values):
        dictionary = {}
        for val in values:
            if val in dictionary.keys():
                dictionary[val] += 1
            else:
                dictionary[val] = 1
        return dictionary
    
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = self.construct_dict(s)
        dict_t = self.construct_dict(t)
        return dict_s == dict_t
