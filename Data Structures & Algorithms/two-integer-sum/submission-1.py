class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        check = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in check:
                check[nums[i]].append(i)
            else:
                check[nums[i]] = [i]

        for i in range(n):
            if target - nums[i] in check:
                if target - nums[i] == nums[i] and len(check[target - nums[i]]) > 1:
                    return check[nums[i]][:2]
                elif target - nums[i] != nums[i]:
                    return [min(i, check[target - nums[i]][0]), max(i, check[target - nums[i]][0])]
        