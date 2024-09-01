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