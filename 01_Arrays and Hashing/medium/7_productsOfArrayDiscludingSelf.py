from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.validateConstraints(nums)
        arr = []
        index = 0
        while index <= len(nums) - 1:
            product = 1
            for i in range(len(nums)):
                if i == index:
                    #index += 1
                    continue
                else:
                    product *= nums[i]
            index += 1
            arr.append(product)
        return arr

    def validateConstraints(self, nums: List[int]) -> bool:
        return

print(Solution().productExceptSelf([1,2,4,6]))
print(Solution().productExceptSelf([-1,0,1,2,3]))


'''
Products of Array Discluding Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
'''