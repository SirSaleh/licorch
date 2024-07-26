# Longest Common Subsequence (LCS)

class Solution(object):

    def from_bottom(self, text1, text2):
        memo = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]        
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                else:
                    memo[i][j] = max(memo[i][j+1], memo[i+1][j])
                print(i, j, memo)
        return memo[0][0]
    
    def from_top(self, text1, text2):
        """
            - - a g f
            - 0 0 0 0  
            b 0
            g 0
            h 0
            f 0
        """
        memo = [[0] * (len(text2) + 1) for x in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[i+1][j+1] = 1 + memo[i][j]
                else:
                    memo[i+1][j+1] = max(memo[i][j+1], memo[i+1][j])
        return memo[len(text1)][len(text2)]

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #self.from_bottom(text1, text2)
        return self.from_top(text1, text2)
        
        

if __name__=="__main__":
    solution = Solution()
    
    q1 = solution.longestCommonSubsequence("abcde", "ace")
    assert q1==3

    q2 = solution.longestCommonSubsequence("abc", "abc")
    assert q2==3

    q3 = solution.longestCommonSubsequence("abc", "def")
    assert q3==0

