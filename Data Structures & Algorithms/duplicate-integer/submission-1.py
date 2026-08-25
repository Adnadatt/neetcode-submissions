# thoughts:
# use non repeat list thing, add if not in, return false if not

# hash set, search is O(1)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for n in nums:
            if n not in numsSet:
                numsSet.add(n)
            else:
                return True
        return False