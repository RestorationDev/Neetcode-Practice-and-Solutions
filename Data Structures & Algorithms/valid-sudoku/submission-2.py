class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #row_dict captures all 9 rows
        row_dict = {}

        #col_arr captures all colums broken separately by dictionary
        col_arr = [{} for _ in range (9)]

        #nei_arr captures all neighborhoods (3x3) broken separately by dictionary
        nei_arr = [{} for _ in range (9)]

        #double loop to parse through 2d arr
        for i, r in enumerate(board):
            for j, elem in enumerate(r):
                #empty element handling
                if elem != ".":
                    
                    #immediate false for elements not 1-9
                    if int(elem) not in range(1,10):
                        return False
                    
                    #since the looping method favors rows, we just have to add it to the dict
                    row_dict[elem] = row_dict.get(elem,0) + 1

                    #specifically adds to jth column since we are looping row wise 
                    col_arr[j][elem] = col_arr[j].get(elem,0) + 1

                    #this last part is the most complicated of the code, find in ipad notes...
                    box_ind = (i // 3) * 3 + (j//3)

                    nei_arr[box_ind][elem] = nei_arr[box_ind].get(elem,0) + 1

                    if row_dict[elem] not in [0,1] or col_arr[j][elem] not in [0,1] or nei_arr[box_ind][elem] not in [0,1]:
                        return False
            row_dict = {}

        return True    


        