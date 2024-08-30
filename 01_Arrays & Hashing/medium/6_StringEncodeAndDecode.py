from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        self.validateConstraints(strs)
        encodedStr = ""
        for s in strs:
            #sCoded = "#" + str(len(s)) + "#" + s
            sCoded = s + "#"
            encodedStr += sCoded
        print("encoded: " + encodedStr)
        print(self.decode(encodedStr))
        return 
    def decode(self, s: str) -> List[str]:
        #decodedList = []
        # for char in s:
        #     if char == "#":
        #         num = num + char
        # s.rsplit("#")
        #    decodedWord = 
        #decodedList.append(decodedWord)
        s = s[:-1]
        return(s.split("#"))
    def validateConstraints(self,strs: List[str]) -> bool:
        return
    

print(Solution().encode(["neet","code","love","you"]))




'''
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''