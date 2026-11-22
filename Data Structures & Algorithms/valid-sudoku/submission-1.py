class Solution:
    def checkNums(self, nums) -> bool:
        # return True is all numbers 1 <= v <= 9

        # remove all the periods / empty spaces
        to_remove = "."
        filtered_nums = list(filter(lambda x: x != to_remove, nums))

        for v in filtered_nums:
            if int(v) > 9 or int(v) < 1:
                return False
        
        
        # check len(set(...)) == same
        return len(set(filtered_nums)) == len(filtered_nums)
        


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board does not need to be full or solvable to be valid
        # 3 conditions:
        # 1. One row has no duplicate number 1-9
        # 2. One column has no duplicate number 1-9
        # 3. one 3x3 quadrant has no duplicate number 1-9

        # approach: O(1). Check each column, row, etc. for 1 <= v <= 9 and len(set(...)) == same
        
        for i in range(9):
            # 1
            row = board[i]
            if self.checkNums(row) == False:
                return False
            
            # 2
            col = [board[j][i] for j in range(9)]
            if self.checkNums(col) == False:
                return False
            
        # 3
        for r in range(3):
            for c in range(3):

                #grid = append(board[r*3:r*3+3][c*3:c*3+3])
                grid = []*9
                for i in range(3):
                    for row in board[(r*3):(r*3+3)]:
                        print(f"{(c*3)},{(c*3+i)}")
                        grid.append(row[c*3+i])
                print(grid)
                if self.checkNums(grid) == False:
                    return False
                    



        return True




        