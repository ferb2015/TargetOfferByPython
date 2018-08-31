"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007

示例：
输入：
1,2,3,4,5,6,7,0

输出：
7
"""
# 归并排序的变形。注意count，设置全局变量，在class外，挺巧妙的。（在牛客网上不能在规定时间内执行完，归并+递归的复杂度还是比较高）

count = 0 
class Solution:
    def InversePairs(self, data):
        global count
        def merge_sort(lists):
            if len(lists) <= 1:
                return lists
            global count 
            def merge(left, right):
                global count
                i, j = 0, 0
                result = []
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        result.append(left[i])
                        i += 1
                    else:
                        result.append(right[j])
                        j += 1
                        count += len(left)-i #right[j]比left[i]小，就比left剩余的都小，因为left是排好序的了
                result += left[i:]
                result += right[j:]
                return result
            # 归并排序
            num = len(lists) >> 1
            left = merge_sort(lists[:num])
            right = merge_sort(lists[num:])
            return merge(left, right)
        merge_sort(data)
        return count%1000000007
