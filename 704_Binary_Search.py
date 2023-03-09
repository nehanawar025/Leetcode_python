class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)-1 
        l,r = 0, size  #pointer to point at indices
                               #for left and right boudaries.

        while l<=r:
                mid = (l+r)//2

                if target < nums[mid]:
                    r = mid-1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    return mid

        return -1
