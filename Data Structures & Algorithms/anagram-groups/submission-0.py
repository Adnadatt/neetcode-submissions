# put the strings into a copy of the list
# sort by length


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = defaultdict(list) # don't need to check for duplicates, can directly append
        for s in strs:
            sortedS = ''.join(sorted(s))
            unique[sortedS].append(s)

        return list(unique.values())