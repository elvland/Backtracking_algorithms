def is_valid_move(grid, row, col, number):
    # Check for three consecutive numbers in rows
    for x in range(max(0, col - 2), min(10, col + 3)):
        if grid[row][x] == number and grid[row][x + 1] == number and grid[row][x + 2] == number:
            return False

    # Check for three consecutive numbers in columns
    for y in range(max(0, row - 2), min(10, row + 3)):
        if grid[y][col] == number and grid[y + 1][col] == number and grid[y + 2][col] == number:
            return False

    # Check if each row and column contains an equal number of zeros and ones
    if check_counts(grid, row, col, number):
        return False

    return True


def check_counts(grid, row, col, number):
    size = len(grid)

    # Count occurrences of zeros and ones in the row after adding the new number
    zero_count_row = sum(1 for x in grid[row] if x == 0) + (1 if number == 0 else 0)
    one_count_row = sum(1 for x in grid[row] if x == 1) + (1 if number == 1 else 0)

    if zero_count_row > size // 2 or one_count_row > size // 2:
        return False

    # Count occurrences of zeros and ones in the column after adding the new number
    zero_count_col = sum(1 for r in range(size) if grid[r][col] == 0) + (1 if number == 0 else 0)
    one_count_col = sum(1 for r in range(size) if grid[r][col] == 1) + (1 if number == 1 else 0)

    if zero_count_col > size // 2 or one_count_col > size // 2:
        return False

    return True


def solve_binox(grid, row, col):
    size = len(grid)

    # Base case: If we have reached the end of the grid, return True
    if row == size:
        return True

    next_row = row + 1 if col == size - 1 else row
    next_col = (col + 1) % size

    # If the current cell is already filled, move to the next cell
    if grid[row][col] != -1:
        return solve_binox(grid, next_row, next_col)

    # Try filling the current cell with 0 and recursively solve
    if is_valid_move(grid, row, col, 0):
        grid[row][col] = 0
        if solve_binox(grid, next_row, next_col):
            return True
        grid[row][col] = -1

    # Try filling the current cell with 1 and recursively solve
    if is_valid_move(grid, row, col, 1):
        grid[row][col] = 1
        if solve_binox(grid, next_row, next_col):
            return True
        grid[row][col] = -1

    # If neither 0 nor 1 can be placed in the current cell, backtrack
    return False




def main():
    if solve_binox(example_grid, 0, 0):
        for i in range(11):
            for j in range(11):
                print(example_grid[i][j], end=" ")
            print()
    else:
        print("no sul")

# Example usage
example_grid = [
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
]
main()