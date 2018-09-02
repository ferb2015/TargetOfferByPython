"""
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

# 这题做了大半天也没有完全AC，就差一点了，最后return的逻辑有问题。
# 最后看的牛客网讨论区的答案。

"""
考虑的点：

1. 不能回到之前经历过的元素，所以要设置一个判断，比如访问过的设为1。并且之后还要复原，比如重新设为0.
2. 递归没有true，能返回到上一个点，又开启新一条路径，我就是在这里始终卡住的。总结就是要设置给false的判断，不能一味地if什么时候为true，还要判断什么时候为false。
"""

class Solution:
    def hasPath(self, matrix, rows, cols, path):       
        # write code here
        flag = [None]*len(matrix)
        def helper(matrix, rows, cols, i, j, path, k, flag):
            index = i * cols + j
            if i<0 or i>=rows or j<0 or j>=cols or matrix[index]!=path[k] or flag[index]==1:
                return False
            if k== len(path) -1:
                return True
            flag[index] = 1
            if (helper(matrix,rows,cols, i-1, j, path, k+1, flag)
                or helper(matrix, rows, cols, i + 1, j, path, k + 1, flag)
                or helper(matrix, rows, cols, i, j - 1, path, k + 1, flag)
                or helper(matrix, rows, cols, i, j + 1, path, k + 1, flag)):
                return True
            flag[index] = 0 
            return False
                            
        for i in range(rows):
            for j in range(cols):
                if helper(matrix,rows,cols,i,j,path,0,flag):
                    return True
        return False
# 或直接写成：

class Solution:
    def hasPath(self, matrix, rows, cols, path):       
        # write code here
        flag = [None]*len(matrix)
        def helper(matrix, rows, cols, i, j, path, flag):
            index = i * cols + j
            if i<0 or i>=rows or j<0 or j>=cols or matrix[index]!=path[0] or flag[index]==1:
                return False
            if len(path)==1:
                return True
            flag[index] = 1
            if (helper(matrix,rows,cols, i-1, j, path[1:], flag)
                or helper(matrix, rows, cols, i + 1, j, path[1:], flag)
                or helper(matrix, rows, cols, i, j - 1, path[1:], flag)
                or helper(matrix, rows, cols, i, j + 1, path[1:], flag)):
                return True
            flag[index] = 0 
            return False
                            
        for i in range(rows):
            for j in range(cols):
                if helper(matrix,rows,cols,i,j,path,flag):
                    return True
        return False
        
a = Solution().hasPath('abcdbdef',2,4,'abb')
print(a)
