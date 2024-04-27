import tkinter as tk

root = tk.Tk()

root.title("NxN Queens")

rows = 16
columns = 16
square_size = 25

def draw_board(canvas, size, rows, cols):
    for row in range(rows):
        for col in range(cols):
            color = "white" if (row + col) % 2 == 0 else "black"
            x1 = col * size
            y1 = row * size
            x2 = x1 + size
            y2 = y1 + size
            canvas.create_rectangle(x1, y1, x2, y2, fill = color)

def can_attack(c, r):
    for q, (col, row) in Queens.items():
        if (col == c) or (row == r) or (abs(col - c) == abs(row - r)):
            return True
    return False


def fill_queens(row, cols):
    if row == rows:
        return True

    for col in range(cols):
        if not can_attack(col, row):
            Queens[row] = (col, row)
            if fill_queens(row + 1, cols):
                return True
            Queens.pop(row)

    return False


def fill(canvas, size, Queens):
    for queen, (col, row) in Queens.items():
        color = "black" if (row + col) % 2 == 0 else "white"
        x = col * size + size / 2
        y = row * size + size / 2
        radius = size / 4
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")

Queens = {}

canvas = tk.Canvas(root, width = columns*square_size, height = rows*square_size)
canvas.pack()

draw_board(canvas, square_size, rows, columns)
fill_queens(0, columns)
fill(canvas,square_size,Queens)

print(Queens)


root.mainloop()