from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.validateConstraints(nums,k)
        numsDict = {}
        resultList = []

        # Place each list number into dictionary
        for x in nums:
            if x not in numsDict:
                numsDict[x] = 1
            else:
                numsDict[x] += 1

        # place max dictionary value into resultList k times
        while k > 0:
            topElement = max(numsDict,key=numsDict.get)
            resultList.append(topElement)
            del numsDict[topElement]
            k -= 1
        return resultList
    
    def validateConstraints(self, nums: List[int], k: int) -> List[int]:
        if not isinstance(nums, list) or not (1 <= len(nums) <= 10000):
            raise Exception("nums must be a list and the length must be between 1 and 10,000")
        distinctiveItems = len(set(nums))
        if not isinstance(k, int) or not (1 <= k <= distinctiveItems):
            raise Exception(f"k must be an integer between 1 and the number of distincive elements in num which is {distinctiveItems}.")
        if not all(isinstance(nums, list) and (-1000 <= i <= 1000) for i in nums):
            raise Exception("nums must be a list and each element in the list must be between -1000 and 1000")

if __name__ == "__main__":
    print(Solution().topKFrequent([1,2,2,3,3,3], 2))
    print(Solution().topKFrequent([7,7], 1))
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))

'''
Top K Elements in List
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
'''
