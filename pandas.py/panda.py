import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Chess Board")

# Board size
rows, cols = 8, 8
square_size = 40  # Size of each square

# Colors
light_color = "#F0D9B5"  # Light brown
dark_color = "#B58863"   # Dark brown

# Chess piece placement
pieces = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["♟"] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    [""] * 8,
    ["♙"] * 8,
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
]

# Create the chessboard
for row in range(rows):
    for col in range(cols):
        color = light_color if (row + col) % 2 == 0 else dark_color
        square = tk.Label(root, bg=color, width=4, height=2, font=("Arial", 24))
        square.grid(row=row, column=col)
        if pieces[row][col]:  # If there's a piece, display it
            square.config(text=pieces[row][col])

# Run the Tkinter event loop
root.mainloop()