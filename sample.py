class Solution:
    def gcdOfStrings(self, str1, str2):
        r = len(str2)
        if str2 in str1:
            return str1[r:]
        return ""
        
s = Solution()
print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))