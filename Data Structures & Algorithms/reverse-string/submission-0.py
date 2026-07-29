class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp=[]

        for i in range(len(s) - 1, -1, -1):
            temp.append(s[i])
        


        for i in range(len(s)):
            s[i]=temp[i]