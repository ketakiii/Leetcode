class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return 

            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                dfs(cur)
                used.remove(i)
        dfs([])
        return res
