'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
# 自己的解法：
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i = 0 
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j] :
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if i < len(nums1):
            for z in range(i,len(nums1)):                
                result.append(nums1[z])
        elif j < len(nums2):
            for z in range(j,len(nums2)):                
                result.append(nums2[z])
        k = len(result) // 2
        if len(result) % 2 ==0:           
            median = (result[k] + result[k-1]) / 2
        else:            
            median = result[k]
        return median
        
     # 官方解法：
     # 
