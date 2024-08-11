
"""Longest Substring without repeating characters


"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        longest_len = 0
        current_chars = set()

        for end in range(len(s)):
            while s[end] in current_chars:
                current_chars.remove(s[start])
                start +=1
            
            current_chars.add(s[end])
            longest_len = max(longest_len, end-start+1)

        return longest_len


if __name__=="__main__":
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb")==3
    assert solution.lengthOfLongestSubstring("bbbbb")==1
    assert solution.lengthOfLongestSubstring("pwwkew")==3