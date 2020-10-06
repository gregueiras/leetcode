class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      i = 0
      lastNum = None
      
      while (i < len(nums)):
        num = nums[i]
        
        if num != lastNum:
          lastNum = num
          i += 1
        else:
          del nums[i]
          
        
        