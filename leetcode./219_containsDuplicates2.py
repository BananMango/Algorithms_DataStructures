class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = {}
        for i in range(len(nums)):
            if nums[i] in hashset.keys():
                if (i - hashset[nums[i]]) <= k:
                    return True
                else:
                    hashset[nums[i]] = i
            else:
                hashset[nums[i]] = i
        return False
