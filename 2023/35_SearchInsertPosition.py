class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        return l
      
      
# return l 
#because if the target value is not there, then for all situation l=mid+1 will be the index
#number where the target value would have take position, if it existed in the list as it is a sorted list.
