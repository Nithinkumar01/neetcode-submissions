class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen={}
        j=0
        for i in range(len(nums)):
            if nums[i] not  in seen:
                seen[nums[i]] = True
            

        i=0    
        for num in seen:
            nums[i]=num
            i+=1;

        return len(seen)
            