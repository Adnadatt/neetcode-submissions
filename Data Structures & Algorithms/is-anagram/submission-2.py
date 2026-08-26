# check length of strings, must be same
# use hashmap, key is the char, value is number of appearances

# looked up:
#   how to loop through a string
#   functions of dictionaries

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charMapS, charMapT= {}, {}
        # for char in s:
        #     charMapS[char] = charMapS.get(char, 0) + 1 # remember this format for initialization
        # for char in t:
        #     charMapT[char] = charMapT.get(char, 0) + 1

        for i in range(len(s)): # can do this bc alr verified length
            charMapS[s[i]] = charMapS.get(s[i], 0) + 1
            charMapT[t[i]] = charMapT.get(t[i], 0) + 1
        
        # for key in charMapS:
        #     if key not in charMapT: # forgot this
        #         return False
        #     if charMapS[key] != charMapT[key]:
        #         return False

        # return True

        return charMapS == charMapT