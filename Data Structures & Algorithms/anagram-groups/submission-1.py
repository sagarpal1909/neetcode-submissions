class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        check  = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            check[tuple(count)].append(s)

        ans = []

        for val in check.values():
            ans.append(val)

        return ans