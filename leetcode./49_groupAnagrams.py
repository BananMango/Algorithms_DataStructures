class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for i in range(len(strs)):
            counter = [0] * 26
            for char in strs[i]:
                counter[ord(char) - ord('a')] += 1
            hashmap[tuple(counter)].append(strs[i])
        return hashmap.values()
