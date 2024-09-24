import numpy as np

# Function to take Sudoku input from the user
def get_sudoku_input():
    sudoku_puzzle = []
    print(" Welcome to Sudoku Sovler!!\n ")
    print("Enter the input as Row 1 : 1 2 4 5 6 3 7 8 9")
    print("Enter your Sudoku puzzle row by row (use 0 for empty cells):")
    
    for i in range(9):
        # Keep asking for input until it's valid
        while True:
            try:
                # Input each row as a space-separated string of 9 numbers
                row = input(f"Row {i+1}: ").strip().split()
                
                # Convert to integers and ensure the row has exactly 9 numbers
                row = [int(num) for num in row]
                
                if len(row) != 9:
                    raise ValueError
                
                # Add the row to the puzzle
                sudoku_puzzle.append(row)
                break
            
            except ValueError:
                print("Invalid input! Please enter 9 integers between 0 and 9 (0 for empty cells).")
    
    return sudoku_puzzle

# Global variable to store Sudoku puzzle
sudoku_puzzle = get_sudoku_input()
solutions = []  # To store all valid solutions

def possible(Row, Column, Num):
    global sudoku_puzzle
    # Is the Num appearing in the given Row?
    for i in range(0, 9):
        if sudoku_puzzle[Row][i] == Num:
            return False

    # Is the Num appearing in the given Column?
    for i in range(0, 9):
        if sudoku_puzzle[i][Column] == Num:
            return False

    # Is the Num appearing in the given square?
    x0 = (Column // 3) * 3
    y0 = (Row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_puzzle[y0 + i][x0 + j] == Num:
                return False

    return True

# Recursive function to find solutions
def solution():
    global sudoku_puzzle, solutions
    for Row in range(0, 9):
        for Column in range(0, 9):
            if sudoku_puzzle[Row][Column] == 0:
                for Num in range(1, 10):
                    if possible(Row, Column, Num):
                        sudoku_puzzle[Row][Column] = Num
                        solution()
                        sudoku_puzzle[Row][Column] = 0
                return

    # Save each solution found
    solutions.append(np.copy(sudoku_puzzle))

# Call the solution function to solve the puzzle
solution()

# Display solutions or notify the user of the number of solutions
def display_solutions():
    if len(solutions) == 0:
        print("No solution found.")
    elif len(solutions) == 1:
        print("\nOnly one solution:")
        print(np.matrix(solutions[0]))
    else:
        for idx, sol in enumerate(solutions):
            print(f"\nSolution {idx + 1}:")
            print(np.matrix(sol))
        
        print(f"\nTotal number of solutions: {len(solutions)}")

# Function to check if user wants to see more solutions
def check_for_more_solutions():
    if len(solutions) == 1:
        print("\nThere is only one solution.")
    else:
        count = 1
        while True:
            user_input = input("\nType 'sol' to see the next solution or 'exit' to stop: ").lower().strip()
            if user_input == 'sol' and count < len(solutions):
                print(f"\nSolution {count + 1}:")
                print(np.matrix(solutions[count]))
                count += 1
            elif user_input == 'sol' and count == len(solutions):
                print("\nNo more solutions. You've seen all the solutions.")
            elif user_input == 'exit':
                print(f"\nTotal number of solutions: {len(solutions)}")
                break
            else:
                print("Invalid input. Please type 'sol' to see the next solution or 'exit' to stop.")

# Display initial solution and ask for more if available
display_solutions()
check_for_more_solutions()


