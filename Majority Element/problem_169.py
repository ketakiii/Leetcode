# -*- coding: utf-8 -*-
"""Problem 169.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xpuuqHzh51WOypOifBiHxffvDTmR1_Sc
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n2 = len(nums)
        
        d1 = dict()
        
        for n in nums:
            if n in d1:
                d1[n] = d1[n] + 1 
            else:
                d1[n] = 1
                
        ans = 0
        for k in d1:
            if d1[k] > n2/2:
                ans = k
        return ans