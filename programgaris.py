import tkinter as tk

# Inisialisasi titik awal dan akhir
start_point = None
end_point = None

# Fungsi untuk menggambar garis menggunakan algoritma Bruteforce
def draw_line_bruteforce(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if x1 == x2:
        y = min(y1, y2)
        while y <= max(y1, y2):
            canvas.create_oval(x1, y, x1 + 1, y + 1, fill="black")
            y += 1
    elif y1 == y2:
        x = min(x1, x2)
        while x <= max(x1, x2):
            canvas.create_oval(x, y1, x + 1, y1 + 1, fill="black")
            x += 1
    elif abs(dx) >= abs(dy):
        m = dy / dx
        x = x1
        while x <= x2:
            y = round(m * (x - x1) + y1)
            canvas.create_oval(x, y, x + 1, y + 1, fill="black")
            x += 1
    else:
        m = dx / dy
        y = y1
        while y <= y2:
            x = round(m * (y - y1) + x1)
            canvas.create_oval(x, y, x + 1, y + 1, fill="black")
            y += 1

# Fungsi untuk menggambar garis menggunakan algoritma DDA
def draw_line_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    step = max(abs(dx), abs(dy))
    x_inc = dx / step
    y_inc = dy / step

    x, y = x1, y1
    for _ in range(int(step) + 1):
        canvas.create_oval(x, y, x + 1, y + 1, fill="black")
        x += x_inc
        y += y_inc

# Fungsi untuk menggambar garis menggunakan algoritma Bresenham
def draw_line_bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    steep = dy > dx
    
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    
    i1 = 2 * dy
    i2 = 2 * (dy - dx)
    d = i1 - dx
    
    if x1 > x2:
        x, y = x2, y2
        xend = x1
    else:
        x, y = x1, y1
        xend = x2
    
    while x <= xend:
        if steep:
            canvas.create_oval(y, x, y + 1, x + 1, fill="black")
        else:
            canvas.create_oval(x, y, x + 1, y + 1, fill="black")

        if d < 0:
            d = d + i1
        else:
            d = d + i2
            y += 1

        x += 1

# Fungsi untuk menggambar lingkaran menggunakan algoritma Bresenham
def draw_circle_bresenham(x_center, y_center, radius):
    x = 0
    y = radius
    d = 3 - 2 * radius

    # Fungsi untuk menggambar 8 simetri titik dari (x, y)
    def plot_circle_points(x_center, y_center, x, y):
        points = [
            (x_center + x, y_center + y),
            (x_center - x, y_center + y),
            (x_center + x, y_center - y),
            (x_center - x, y_center - y),
            (x_center + y, y_center + x),
            (x_center - y, y_center + x),
            (x_center + y, y_center - x),
            (x_center - y, y_center - x)
        ]
        
        # Menampilkan titik pada canvas dan memperbarui koordinat di GUI
        for (px, py) in points:
            canvas.create_oval(px, py, px + 1, py + 1, fill="black")
            # Update label untuk menampilkan koordinat
            coordinates_label.config(text=f"Koordinat: ({px}, {py})")
            window.update_idletasks()  # Memperbarui tampilan GUI secara langsung

    # Gambar titik-titik lingkaran menggunakan simetri delapan
    plot_circle_points(x_center, y_center, x, y)

    while x < y:
        x += 1
        if d < 0:
            d = d + 4 * x + 6
        else:
            y -= 1
            d = d + 4 * (x - y) + 10
        plot_circle_points(x_center, y_center, x, y)

# Fungsi untuk menangani klik pada canvas
def on_canvas_click(event):
    global start_point, end_point
    algorithm = algorithm_var.get()
    
    if algorithm == "Lingkaran":
        x_center = event.x
        y_center = event.y
        radius = 50
        draw_circle_bresenham(x_center, y_center, radius)
    else:
        if start_point is None:
            start_point = (event.x, event.y)
            start_label.config(text=f"Titik Awal: ({start_point[0]}, {start_point[1]})")
        else:
            end_point = (event.x, event.y)
            end_label.config(text=f"Titik Akhir: ({end_point[0]}, {end_point[1]})")
            x1, y1 = start_point
            x2, y2 = end_point
            
            if algorithm == "Bruteforce":
                draw_line_bruteforce(x1, y1, x2, y2)
            elif algorithm == "DDA":
                draw_line_dda(x1, y1, x2, y2)
            elif algorithm == "Bresenham":
                draw_line_bresenham(x1, y1, x2, y2)
            
            start_point = None
            end_point = None

# Fungsi untuk membersihkan canvas
def clear_canvas():
    canvas.delete("all")
    start_label.config(text="Titik Awal: (0, 0)")
    end_label.config(text="Titik Akhir: (0, 0)")
    coordinates_label.config(text="Koordinat: (0, 0)")  # Reset koordinat lingkaran

# GUI Tkinter
window = tk.Tk()
window.title("Program Menggambar Garis dan Lingkaran")

frame = tk.Frame(window)
frame.pack()

algorithm_var = tk.StringVar(value="Bruteforce")
tk.Radiobutton(frame, text="Algoritma Garis Bruteforce", variable=algorithm_var, value="Bruteforce").pack(side="left")
tk.Radiobutton(frame, text="Algoritma Garis DDA", variable=algorithm_var, value="DDA").pack(side="left")
tk.Radiobutton(frame, text="Algoritma Garis Bresenham", variable=algorithm_var, value="Bresenham").pack(side="left")
tk.Radiobutton(frame, text="Algoritma Lingkaran Bresenham", variable=algorithm_var, value="Lingkaran").pack(side="left")

canvas = tk.Canvas(window, width=500, height=500, bg="white")
canvas.pack()

coordinates_label = tk.Label(window, text="Koordinat: (0, 0)", font=("Arial", 12))
coordinates_label.pack()

start_label = tk.Label(window, text="Titik Awal: (0, 0)", font=("Arial", 12))
start_label.pack()

end_label = tk.Label(window, text="Titik Akhir: (0, 0)", font=("Arial", 12))
end_label.pack()

clear_button = tk.Button(window, text="Clear Canvas", command=clear_canvas)
clear_button.pack()

canvas.bind("<Button-1>", on_canvas_click)

window.mainloop()
