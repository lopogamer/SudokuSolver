import os
import tkinter as tk
from tkinter import messagebox
import subprocess

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        
        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j)
                entry.bind("<Key>", self.handle_key)
                row.append(entry)
            self.entries.append(row)

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9)
        
        self.current_row = 0
        self.current_col = 0
        self.entries[0][0].focus_set() 

    def handle_key(self, event):
        key = event.keysym

        if key == "Up":
            self.move_focus(-1, 0)
        elif key == "Down":
            self.move_focus(1, 0)
        elif key == "Left":
            self.move_focus(0, -1)
        elif key == "Right":
            self.move_focus(0, 1)

    def move_focus(self, row_offset, col_offset):
        new_row = (self.current_row + row_offset) % 9
        new_col = (self.current_col + col_offset) % 9

        self.current_row = new_row
        self.current_col = new_col

        self.entries[self.current_row][self.current_col].focus_set()

    def solve(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        input_path = os.path.join(current_dir, '../input.txt')
        output_path = os.path.join(current_dir, '../output.txt')
        solver_path = os.path.join(current_dir, '../backtracking/solver.exe')

        with open(input_path, "w") as f:
            for i in range(9):
                for j in range(9):
                    value = self.entries[i][j].get()
                    if value == "":
                        f.write("0 ")
                    else:
                        f.write(value + " ")
                f.write("\n")
        
        subprocess.run([solver_path])
        
        with open(output_path, "r") as f:
            solution = f.readlines()
        
        if solution[0].strip() == "No solution":
            messagebox.showerror("Error", "No solution exists for the given Sudoku!")
        else:
            for i in range(9):
                numbers = solution[i].strip().split()
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, numbers[j])

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
