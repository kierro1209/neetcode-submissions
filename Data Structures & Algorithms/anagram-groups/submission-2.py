from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #encountering an unknown key creates a new empty list
        for s in strs:
            sortedS = ''.join(sorted(s)) #creates sorted key
            res[sortedS].append(s) #sorts into sorted key, if not in existence, creates new list and appends element
        return list(res.values()) #get values of hashmap and puts them into a list

        

        