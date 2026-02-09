class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list) #dict of list values

        for s in strs:
            count = [0]*26 # creates [0,0,0,....] 26 times
            for char in s: 
                index = ord(char) - ord('a') #for each word, lets say "bat" for each letter 98 ( b ascii value) - 97 (a ascii value) = 1 will be appended to the list
                count[index]+=1 #so the list will look [ 1, 1, 0,0, 0,...]
            key = tuple(count) #conversion to tuple since dict wont accept lists for keys
            groups[key].append(s) #now assign the word for the key, multiple words will be assigned for same key for anagrams

        return list(groups.values()) #returning list of lists of values

        
        