class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups ={}

        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word) #add the word to the list stored at that key 
            else:
                groups[key]= [word]
        return list(groups.values())