class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = {}
        for i in range(len(nums1)):
            if nums1[i] in hashset.keys():
                hashset[nums1[i]] += 1
            else:
                hashset[nums1[i]] = 1
            
        res = list()
        for i in range(len(nums2)):
            if nums2[i] in hashset.keys() and hashset[nums2[i]] > 0:
                res.append(nums2[i])
                hashset[nums2[i]] -= 1
        return res
            
