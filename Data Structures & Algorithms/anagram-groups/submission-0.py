class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        check = {}

        for i in range(len(strs)):
            res = "".join(sorted(strs[i]))
            if res in check:
                check[res].append(i)
            else:
                check[res] = [i]

        ans = []

        for k,v in check.items():
            res = []
            for i in v:
                res.append(strs[i])

            ans.append(res)


        return ans
        