# 都要区分开左右子树，核心思想，重点1.怎么区分开。重点2.怎么判断true false

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence==None or len(sequence)<=0:
            return False
        root = sequence[-1]
        for i in sequence:
            if i>root:
                break
        j = sequence.index(i)   #左右子树区分点
        for ii in sequence[j:]:
            if ii < root:
                return False
        left,right = True, True
        if j>0: #之前没写这个判断  不是全部都是右子树 也有左子树 才执行下面一步
            left = self.VerifySquenceOfBST(sequence[:j])
        if j<len(sequence)-1:    #不是全部都是左子树 也有右子树 才执行下面一步 （如果全部都是左子树， j==len(sequence)-1
            right = self.VerifySquenceOfBST(sequence[j:-1])
        return left and right
