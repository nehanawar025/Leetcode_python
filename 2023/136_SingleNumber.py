class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unqVal = 0
        for itr in nums:
            unqVal ^= itr
        return unqVal
