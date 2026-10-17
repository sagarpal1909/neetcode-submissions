class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ans = 0
        check = set(nums)

        for num in nums:
            count = 0
            if num - 1 not in check:
                while num in check:
                    num += 1
                    count += 1

            ans = max(ans, count)

        return ans
        