# Using Hashmap

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}   

        for key in nums:
            if key in hashmap:
                return True
            hashmap[key] = 1 
        return False

        
#  Accepted -------------------------------      

# Using Hashset

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for key in nums:
            if key in hashset:
                return True
            else:
                hashset.add(key)
        
# Accepted ----------------------------------


