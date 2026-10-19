# maybe use a hashset (no duplicates)
# search sequentially through the string
# pointer i (beginning)
# if find duplicate, compare with maxLength

# only need the string of characters from one duplicate to char before next duplicate

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        longest = 0
        chars = set()
        l = 0
        
        for r in range(len(s)):
            while s[r] in chars:
                # increment l until no duplicate
                
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            longest = max(longest, r - l + 1)

        return longest