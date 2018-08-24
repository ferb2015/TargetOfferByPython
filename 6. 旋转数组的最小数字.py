# 数组中的第一个数大于等于最后一个数，用二分查找，看中间值和第一个数比较，如果比第一个大，那肯定是前面是递增的。

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        if len(rotateArray)==1:
            return rotateArray[0]
        if len(rotateArray)==2:
            if rotateArray[0]<=rotateArray[1]:
                return rotateArray[0]
            else:
                return rotateArray[1] 
        #start = rotateArray[0]
        #stop = rotateArray[len(rotateArray[0])-1]        
        index = int(len(rotateArray)/2)
        middle = rotateArray[index]
        if middle>=rotateArray[0] :
            return self.minNumberInRotateArray(rotateArray[index:])
        else:
            return self.minNumberInRotateArray(rotateArray[:index+1]) 
S = Solution()
p = S.minNumberInRotateArray([3,3,3,1,3])
print(p)
