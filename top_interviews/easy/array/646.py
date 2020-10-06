class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) < k):
            for _ in range(k):
                for i in reversed(range(1, len(nums))):
                    nums[i-1:i+1] = nums[i-1:i+1][::-1]

        nums[:] = reversed(nums)
        nums[k:] = reversed(nums[k:])
        nums[:k] = reversed(nums[:k:])
          
        