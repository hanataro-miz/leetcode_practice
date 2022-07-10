# from sparshlodha04's answer
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):
            mat[i] = (i,mat[i])
        mat.sort(key = lambda x: x[1].count(1))
        return [mat[i][0] for i in range(k)]
