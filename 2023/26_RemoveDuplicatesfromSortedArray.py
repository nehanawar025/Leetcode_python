class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u_val = 0
        for itr in range(1,len(nums)):
            if nums[itr] == nums[itr-1]:
                itr = itr+1
            else:
                u_val = u_val + 1
                nums[u_val] = nums[itr]
                itr = itr + 1
        
        return u_val+1
