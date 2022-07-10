class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        val_list = []
        weak_list = []
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[1])):
                if mat[i][j] == 1:
                    count += 1
            val_list.append(count)
            count = 0
        print(val_list)
        
        min_index = 0
        for i in range(len(val_list)):
            for j in range(len(val_list)):
                if val_list[min_index] > val_list[j]:
                    min_index = j
            weak_list.append(min_index)
            val_list[min_index] = 2048  # 番兵
            print(val_list)
            min_index = 0
        return weak_list[:k]
