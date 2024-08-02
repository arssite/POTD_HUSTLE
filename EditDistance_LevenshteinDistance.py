# https://leetcode.com/problems/edit-distance/

class Solution:
    def editDistance(self, str1, str3):
        # Code here
        n=len(str1)
        m=len(str3)
        dp=[0]*(m+1)
        for i in range(1,m+1):
            dp[i]=i
        for i in range(1,n+1):
            prev=dp[0]
            dp[0]=i
            for j in range(1,m+1):
                temp=dp[j]
                if str1[i-1]==str3[j-1]:
                    dp[j]=prev
                else:
                    dp[j]=1+min(dp[j],prev,dp[j-1])
                prev=temp
        return dp[-1]

#memo
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
            
        memo = {}
        
        def Recur(w1, w2):
            if (w1, w2) in memo:
                return memo[(w1, w2)]
            
            if not w1:
                return len(w2)
            if not w2:
                return len(w1)
            
            if w1[0] == w2[0]:
                result = Recur(w1[1:], w2[1:])
            else:
                insert = Recur(w1, w2[1:]) + 1
                delete = Recur(w1[1:], w2) + 1
                replace = Recur(w1[1:], w2[1:]) + 1
                result = min(insert, delete, replace)
            
            memo[(w1, w2)] = result
            return result
        
        return Recur(word1, word2)
