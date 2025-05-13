def solve_n_queens(n):
    solutions = []
    def backtrack(row, columns, diag1, diag2, board):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return
        
        for col in range(n):
            if col in columns or (row - col) in diag1 or (row + col) in diag2:
                continue 
            
            board[row][col] = 'Q'
            columns.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            backtrack(row + 1, columns, diag1, diag2, board)
            board[row][col] = '.'
            columns.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    empty_board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return solutions
n = 4
results = solve_n_queens(n)
print(f"Total Solutions for N={n}:", len(results))
for i, solution in enumerate(results, 1):
    print(f"\nSolution {i}:")
    for row in solution:
        print(row)
print("\nTime Complexity:")
print("- Worst case: O(N!) due to N choices per row (reduced by pruning)")
print("- Constraint propagation using sets for columns and diagonals reduces unnecessary recursion")
