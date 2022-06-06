# -*- coding: utf-8 -*-
"""Problem 409.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xpuuqHzh51WOypOifBiHxffvDTmR1_Sc
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        total = 0
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        p = list(freq.values())
        print(p)

        total = 0
        odd = 0 

        if len(s) == 1:
            return freq[s[0]] 

        else:
            for i in freq.values():
                if i > 1:
                    if i % 2 == 0:
                        total += i 
                    else:
                        total += i-1
                        odd += 1
                else:
                    odd += 1
    
        if odd > 0:
                total += 1

        return total