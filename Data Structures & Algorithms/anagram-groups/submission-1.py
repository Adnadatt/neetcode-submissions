# referenced the solution for this, must come back & retry

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = defaultdict(list) # don't need to check for duplicates, can directly append
        for s in strs:
            sortedS = ''.join(sorted(s)) # sorted(s) = ['a','b','c'], joins to 'abc'
            unique[sortedS].append(s) # using the sorted string as the key, append s

        return list(unique.values())