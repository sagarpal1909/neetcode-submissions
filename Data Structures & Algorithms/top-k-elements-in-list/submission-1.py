class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        check = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            check[num] = 1 + check.get(num, 0)

        for num, count in check.items():
            freq[count].append(num)

        # print(freq)

        ans = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        
        