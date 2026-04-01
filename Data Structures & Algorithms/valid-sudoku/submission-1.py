class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row_dict = {i: 0 for i in range(1,10)}

        row_dict = {}
        col_arr = [{} for _ in range (9)]
        nei_arr = [{} for _ in range(9)]

        #col_arr = [{i: 0 for i in range(1,10)} for _ in range (4)]


        for i, r in enumerate(board):
            for j, elem in enumerate(r):
                if elem != ".":
                    if int(elem) not in range(1,10):
                        return False
                    row_dict[elem] = row_dict.get(elem,0) + 1
                    col_arr[j][elem] = col_arr[j].get(elem,0) + 1
                    box_ind = (i // 3) * 3 + (j // 3)
                    nei_arr[box_ind][elem] = nei_arr[box_ind].get(elem,0) + 1

                    if row_dict[elem] not in [0,1] or col_arr[j][elem] not in [0,1] or nei_arr[box_ind][elem] not in [0,1]:
                        print(row_dict)
                        print(col_arr)
                        print(nei_arr)
                        return False
            row_dict = {}
            
        return True



