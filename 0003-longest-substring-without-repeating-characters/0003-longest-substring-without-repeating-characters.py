class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         unique_str = ''
#         for i in range(len(s)):
#             if s[i] not in unique_str:
#                 unique_str += s[i]
#                 str_set = set (unique_str)
                
#         return len(str_set)

            char_set = set()  # To store unique characters in the current substring
            left = 0  # The starting point of the sliding window
            max_len = 0  # To store the maximum length of substring without repeating characters

            for right in range(len(s)):
                # If the character is already in the set, shrink the window from the left
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1

                # Add the current character to the set
                char_set.add(s[right])

                # Update the maximum length
                max_len = max(max_len, right - left + 1)

            return max_len