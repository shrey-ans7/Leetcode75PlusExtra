class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # skip duplicates at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # prune: numbers are positive and sorted
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                dfs(i + 1, remain - candidates[i])  # i+1: each element used at most once
                path.pop()

        dfs(0, target)
        return res
