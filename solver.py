# solver.py
board = [
                    [3,0,0,8,0,0,0,0,1],
                    [0,0,0,0,0,2,0,0,0],
                    [0,4,1,5,0,0,8,3,0],
                    [0,2,0,0,0,1,0,0,0],
                    [8,5,0,4,0,3,0,1,7],
                    [0,0,0,7,0,0,0,2,0],
                    [0,8,5,0,0,9,7,4,0],
                    [0,0,0,1,0,0,0,0,0],
                    [9,0,0,0,0,7,0,0,6]
]

def print_board(brd):

   for i in range(len(brd)):
       if i%3==0 and i !=0:
           print("- - - - - - - - - - - - ")

       for j in range(len(brd[0])):
            if j%3==0 and  j!=0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")

def find_empty(brd):
     for i in range(len(brd)):
         for j in range(len(brd[0])):
             if brd[i][j] == 0:
                return (i,j)
     return None

def brd_valid(brd, num, pos):
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1]!=1:
            return False

    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    cube_x = pos[1] // 3
    cube_y =  pos[0] // 3

    for i in range(cube_y*3, cube_y*3 +3):
        for j in range(cube_x*3, cube_x*3 + 3):
            if brd[i][j] == num and (i,j) !=pos:
                return False

    return True

def solve_board(brd):
    #base case
    empty_spot = find_empty(brd)
    if not empty_spot:
        return True
    else:
        row, col = empty_spot

    for i in range(1,10):
        if brd_valid(brd, i, (row,col)):
            brd[row][col] = i

            if solve_board(brd):
                return True
            brd[row][col] = 0

    return False

#displaying the sudoku solver
print_board(board)
solve_board(board)
print("**********************")
print("***Solved Answer******")
print_board(board)
