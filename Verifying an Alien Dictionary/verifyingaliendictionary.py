class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # dictionary of order
        orderdict = {element: index for index, element in enumerate(order)}
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(len(word1)):
                # condition 1 - len of word2 is less than word1
                if j == len(word2):
                    return False 
                # condition 2 - word1 char > word2 char
                if word1[j] != word2[j]:
                    if orderdict[word1[j]] > orderdict[word2[j]]:
                        return False 
                    break 
        return True 

            
