class Solution:
    def twoSum(self, nums, target) -> List[int]:
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i+1,len(nums)):
                    num2 = nums[j]
                    if num1 + num2 == target:
                        return [i,j]
                        
# Runtime: 5264 ms, Memory Usage: 13.8 MB

class Solution:
    def twoSum(self, nums, target) -> List[int]:
        dictionary = dict()  
        pos = 0
        while pos< len(nums) :
            if target-nums[pos] not in dictionary:
                dictionary[nums[pos]] = pos
                pos += 1
            else:
                return [dictionary[target-nums[pos]],pos]
                
 # Runtime: 56 ms,Memory Usage: 14.5 MB
