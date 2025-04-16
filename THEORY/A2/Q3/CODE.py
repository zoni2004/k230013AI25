
import sys
from collections import deque

def read_sudoku():
    sudoku = []
    for _ in range(9):
        line = sys.stdin.readline().strip()
        row = []
        for c in line:
            if c == '.':
                row.append(0)
            else:
                row.append(int(c))
        sudoku.append(row)
    return sudoku

def print_sudoku(sudoku):
    for row in sudoku:
        print(''.join(map(str, row)))

def get_subgrid(sudoku, row, col):
    subgrid = []
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            subgrid.append(sudoku[start_row + i][start_col + j])
    return subgrid

def is_valid(sudoku, row, col, num):
    # Check row
    if num in sudoku[row]:
        return False
    # Check column
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    # Check subgrid
    subgrid = get_subgrid(sudoku, row, col)
    if num in subgrid:
        return False
    return True

def find_empty_cell(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(sudoku):
    empty_cell = find_empty_cell(sudoku)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0
    return False

def main():
    sudoku = read_sudoku()
    if solve_sudoku(sudoku):
        print_sudoku(sudoku)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()
