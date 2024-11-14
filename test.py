import tkinter as tk

# Fungsi untuk menggambar garis dengan algoritma Brute Force
def draw_bruteforce_line(canvas, x1, y1, x2, y2):
    # Kasus garis vertikal
    if x1 == x2:
        x = x1
        y = min(y1, y2)
        while y <= max(y1, y2):
            canvas.put("#000000", (x, y))  # Gambar titik (warna hitam)
            y += 1
        return
    
    # Kasus garis horizontal
    if y1 == y2:
        y = y1
        x = min(x1, x2)
        while x <= max(x1, x2):
            canvas.put("#000000", (x, y))  # Gambar titik (warna hitam)
            x += 1
        return

    # Tukar titik jika x2 < x1
    if x2 < x1:
        x1, y1, x2, y2 = x2, y2, x1, y1

    # Hitung kemiringan garis
    m = (y2 - y1) / (x2 - x1)

    # Kasus |m| <= 1: Pencacahan melalui x
    if abs(m) <= 1:
        N = x2 - x1 + 1
        x, y = x1, y1
        for _ in range(N):
            ya = round(m * (x - x1) + y1)  # Pembulatan hasil y
            canvas.put("#000000", (x, ya))  # Gambar titik (warna hitam)
            x += 1
    # Kasus |m| > 1: Pencacahan melalui y
    else:
        if y2 < y1:
            x1, y1, x2, y2 = x2, y2, x1, y1  # Pastikan y1 < y2
        N = y2 - y1 + 1
        y, x = y1, x1
        for _ in range(N):
            xa = round((y - y1) / m + x1)  # Pembulatan hasil x
            canvas.put("#000000", (xa, y))  # Gambar titik (warna hitam)
            y += 1

# GUI Tkinter untuk antarmuka garis Brute Force
def bruteforce_interface():
    window = tk.Tk()
    window.title("Algoritma Garis Bruteforce")

    # Canvas untuk menggambar garis
    canvas = tk.PhotoImage(width=500, height=500)
    canvas_label = tk.Label(window, image=canvas)
    canvas_label.pack()

    # Koordinat titik
    x1, y1, x2, y2 = 50, 50, 400, 300  # Anda bisa mengganti titik ini

    # Menggambar garis dengan algoritma Brute Force
    draw_bruteforce_line(canvas, x1, y1, x2, y2)

    window.mainloop()

# Jalankan antarmuka Brute Force
bruteforce_interface()
