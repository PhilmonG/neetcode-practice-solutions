class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sDict = {}
            tDict = {}
            for char in s:
                if char in sDict:
                    sDict[char] += 1
                else:
                    sDict[char] = 1
            
            for char in t:
                if char in tDict:
                    tDict[char] += 1
                else:
                    tDict[char] = 1

            if sDict.items() == tDict.items():
                return True
        return False




s = "jam"
t = "jar"
result = Solution().isAnagram(s,t)
print(result)