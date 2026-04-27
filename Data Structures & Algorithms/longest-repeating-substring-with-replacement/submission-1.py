from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n, mp = len(s), defaultdict(int) 
        longest_len = l = max_freq = 0

        for r in range(n):
            # update the counter based on what we see
            # as we iterate 
            mp[s[r]] = 1 + mp[s[r]]

            # update the max possible replacement
            max_freq = max(
                max_freq, 
                mp[s[r]] 
            )

            # we have more characters than 
            # the possible we can replace
            # meaning that we need to shrink 
            # the window size until we get 
            # a valid window size
            while (r - l + 1) - max_freq > k:
                # reduce the amount left
                # as we replaced that character 
                mp[s[l]] -= 1

                # update the pointer to be 
                # a character that has not yet 
                # been replaced
                l += 1

            # calculate the longest 
            # length
            longest_len = max(
                longest_len,
                r - l + 1
            )

        return longest_len


# Idea: The goal is to find the longest window
# where all characters use at most k replacement 
# window-size --> count of most frequent character <= k
# b/c characters that are not frequent are the ones that 
# we need to replace. Thus, as we expand the window we 
# track: 1) frequency of each character 2) most frequent 
# character inside the winow. 

# if the window becomes invalid, we shrink the left.
# time: O(n), space: O(m), where n is len of string & 
# m is the total of unique characters in the string
        




