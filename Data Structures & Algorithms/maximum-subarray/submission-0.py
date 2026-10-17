class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = -sys.maxsize
        pre = 0

        for num in nums:
            pre += num
            ans = max(ans, pre)
            if pre < 0:
                pre = 0

        return ans
        