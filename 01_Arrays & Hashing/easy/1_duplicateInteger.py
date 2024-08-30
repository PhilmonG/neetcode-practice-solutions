from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        theSet = set()
        for x in nums:
            if x in theSet:
                return True
            theSet.add(x)
        return False
    

numList = [1, 2, 3, 4]
result = Solution().hasDuplicate(nums=numList)
print(result)
# using a set instead of a dictionary because there is no need to store a value, only check for uniqueness. we only store key, not key-value pair.