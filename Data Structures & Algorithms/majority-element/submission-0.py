class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       value = len(nums)
       for i in range(len(nums)):
            count =0 
            for j in range(len(nums)):

                if nums[i] == nums[j]:
                    count +=1

            
            if count > value / 2:
                return nums[i]
                        

