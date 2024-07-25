# Longest Common Subsequence (LCS)

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        memo = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]        
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                else:
                    memo[i][j] = max(memo[i][j+1], memo[i+1][j])
                print(i, j, memo)
        return memo[0][0]
        

if __name__=="__main__":
    solution = Solution()
    
    q1 = solution.longestCommonSubsequence("abcde", "ace")
    assert q1==3

    q2 = solution.longestCommonSubsequence("abc", "abc")
    assert q2==3

    q3 = solution.longestCommonSubsequence("abc", "def")
    assert q3==0

