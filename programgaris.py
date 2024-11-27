import tkinter as tk

# Inisialisasi titik awal dan akhir
start_point = None
end_point = None


def draw_line_bruteforce(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Tukar titik awal dan akhir agar x1 selalu <= x2 untuk konsistensi
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        dx = -dx
        dy = -dy

    # garis vertikal
    if x1 == x2:
        y_step = 1 if y1 < y2 else -1
        y = y1
        while y != y2 + y_step:
            canvas.create_oval(x1, y, x1 + 1, y + 1, fill="black")
            y += y_step

    # garis horizontal
    elif y1 == y2:
        x = min(x1, x2)
        while x <= max(x1, x2):
            canvas.create_oval(x, y1, x + 1, y1 + 1, fill="black")
            x += 1

    # pencacahan melalui x
    elif abs(dx) >= abs(dy):
        m = dy / dx
        y_step = 1 if y1 < y2 else -1
        x = x1
        while x <= x2:
            y = round(m * (x - x1) + y1)
            canvas.create_oval(x, y, x + 1, y + 1, fill="black")
            x += 1

    # pencacahan melalui y
    else:
        m = dx / dy
        y_step = 1 if y1 < y2 else -1
        y = y1
        while y != y2 + y_step:
            x = round(m * (y - y1) + x1)
            canvas.create_oval(x, y, x + 1, y + 1, fill="black")
            y += y_step



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


def draw_line_bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Tentukan apakah gradien lebih besar dari 1 (vertikal)
    steep = dy > dx
    
    if steep:
        # Tukar x dan y jika gradien > 1
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    
    # Tentukan arah inkremen y berdasarkan posisi y1 dan y2
    y_step = 1 if y1 < y2 else -1
    
    # Tentukan arah inkremen x berdasarkan posisi x1 dan x2
    x_step = 1 if x1 < x2 else -1

    # Variabel keputusan
    i1 = 2 * dy
    i2 = 2 * (dy - dx)
    d = i1 - dx
    
    # Inisialisasi titik awal dan akhir
    x, y = x1, y1
    
    # Gambar titik pada posisi awal
    if steep:
        canvas.create_oval(y, x, y + 1, x + 1, fill="black")
    else:
        canvas.create_oval(x, y, x + 1, y + 1, fill="black")
    
    # Gambar garis dari titik awal ke titik akhir
    if x1 == x2:  # Jika garis vertikal
        while y != y2:
            y += y_step
            if steep:
                canvas.create_oval(y, x, y + 1, x + 1, fill="black")
            else:
                canvas.create_oval(x, y, x + 1, y + 1, fill="black")
    else:  # Jika garis miring atau horizontal
        while x != x2:
            if d < 0:
                d += i1
            else:
                d += i2
                y += y_step  # Tambah atau kurangi y sesuai arah
            
            x += x_step  # Mengatur inkremen x sesuai arah
            
            # Gambar titik saat ini pada koordinat (x, y)
            if steep:
                canvas.create_oval(y, x, y + 1, x + 1, fill="black")
            else:
                canvas.create_oval(x, y, x + 1, y + 1, fill="black")
    
    # Gambar titik akhir
    if steep:
        canvas.create_oval(y2, x2, y2 + 1, x2 + 1, fill="black")
    else:
        canvas.create_oval(x2, y2, x2 + 1, y2 + 1, fill="black")



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


def clear_canvas():
    canvas.delete("all")
    start_label.config(text="Titik Awal: (0, 0)")
    end_label.config(text="Titik Akhir: (0, 0)")
    coordinates_label.config(text="Koordinat: (0, 0)")  # Reset koordinat lingkaran

# GUI Tkinter
window = tk.Tk()
window.title("Program Menggambar Garis dan Lingkaran")

# Frame untuk menu algoritma 
menu_frame = tk.Frame(window)
menu_frame.pack(side="top", fill="x", padx=10, pady=10)  # Menempatkan frame di atas

# Membuat pilihan algoritma dalam menu_frame 
algorithm_var = tk.StringVar(value="Bruteforce")
tk.Radiobutton(menu_frame, text="Algoritma Garis Bruteforce", variable=algorithm_var, value="Bruteforce").pack(side="left", padx=5)
tk.Radiobutton(menu_frame, text="Algoritma Garis DDA", variable=algorithm_var, value="DDA").pack(side="left", padx=5)
tk.Radiobutton(menu_frame, text="Algoritma Garis Bresenham", variable=algorithm_var, value="Bresenham").pack(side="left", padx=5)
tk.Radiobutton(menu_frame, text="Algoritma Lingkaran Bresenham", variable=algorithm_var, value="Lingkaran").pack(side="left", padx=5)

# Frame untuk canvas dan elemen lainnya di bawah menu
content_frame = tk.Frame(window)
content_frame.pack(side="top", padx=10, pady=10)

# Canvas untuk menggambar
canvas = tk.Canvas(content_frame, width=500, height=500, bg="white")
canvas.pack()

# Frame untuk koordinat dan tombol Clear
button_frame = tk.Frame(content_frame)
button_frame.pack(side="top", fill="x", padx=10, pady=5)

# Label untuk menampilkan koordinat
coordinates_label = tk.Label(button_frame, text="Koordinat: (0, 0)", font=("Arial", 12))
coordinates_label.pack(side="top", padx=5)

# Label untuk titik awal
start_label = tk.Label(button_frame, text="Titik Awal: (0, 0)", font=("Arial", 12))
start_label.pack(side="left", padx=5)

# Label untuk titik akhir
end_label = tk.Label(button_frame, text="Titik Akhir: (0, 0)", font=("Arial", 12))
end_label.pack(side="left", padx=5)

# Tombol untuk membersihkan canvas
clear_button = tk.Button(button_frame, text="Clear Canvas", command=clear_canvas)
clear_button.pack(side="left", padx=5)

# Menangani klik pada canvas
canvas.bind("<Button-1>", on_canvas_click)

window.mainloop()

