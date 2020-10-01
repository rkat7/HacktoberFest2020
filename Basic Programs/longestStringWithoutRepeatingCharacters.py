#Leetcode's Longest String Without Repeating Characters solution in python
#Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        fl=[]
        for i in range(len(s)):
            l=[]
            for j in range(i,len(s)):
                if s[j] not in l:
                    l.append(s[j])
                    
                else:
                    break
            fl.append(len(l))
        
        return max(fl)
    
        
