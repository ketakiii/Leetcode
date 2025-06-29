class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_of_words = s.split(' ') 
        words = []
        for i in list_of_words:
            if i != '':
                words.append(i)
        return len(words[-1])
