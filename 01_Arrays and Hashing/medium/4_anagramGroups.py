from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sortedWord = tuple(sorted(word))
            if sortedWord not in anagrams:
                anagrams[sortedWord] = []
            # anagrams[sortedWord].append(word)
            anagrams[sortedWord].append(word)
        return list(anagrams.values())
    


inputStrs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs=inputStrs))

'''Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.'''