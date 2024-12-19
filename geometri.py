import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

def baca_csv_titik(file):
    titik = []
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Lewati header
            for row in reader:
                titik.append([float(row[0]), float(row[1]), float(row[2]), 1])  
    except Exception as e:
        messagebox.showerror("Error Membaca File", f"Gagal membaca file {file}: {e}")
    return np.array(titik)

def baca_csv_garis(file):
    garis = []
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Lewati header
            for row in reader:
                garis.append(tuple(map(int, row)))
    except Exception as e:
        messagebox.showerror("Error Membaca File", f"Gagal membaca file {file}: {e}")
    return garis

def dda(canvas, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        canvas.create_oval(int(x), int(y), int(x) + 1, int(y) + 1, fill="black")
        x += x_inc
        y += y_inc

def transformasi_3d(titik, matriks_transformasi):
    return np.dot(titik, matriks_transformasi.T)

def matriks_skala(faktor):
    return np.array([
        [faktor, 0, 0, 0],
        [0, faktor, 0, 0],
        [0, 0, faktor, 0],
        [0, 0, 0, 1]
    ])

def matriks_rotasi(sudut, sumbu):
    sudut_rad = np.radians(sudut)
    cos_theta = np.cos(sudut_rad)
    sin_theta = np.sin(sudut_rad)

    if sumbu == 'x':
        return np.array([
            [1, 0, 0, 0],
            [0, cos_theta, -sin_theta, 0],
            [0, sin_theta, cos_theta, 0],
            [0, 0, 0, 1]
        ])
    elif sumbu == 'y':
        return np.array([
            [cos_theta, 0, sin_theta, 0],
            [0, 1, 0, 0],
            [-sin_theta, 0, cos_theta, 0],
            [0, 0, 0, 1]
        ])
    elif sumbu == 'z':
        return np.array([
            [cos_theta, -sin_theta, 0, 0],
            [sin_theta, cos_theta, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

def matriks_translasi(dx, dy, dz):
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])

def gambar_garis():
    canvas.delete("all")

    global titik
    titik_dilatasi = transformasi_3d(titik, matriks_skala(50))

    for g in garis:
        if g[0] < 1 or g[1] < 1 or g[0] > len(titik_dilatasi) or g[1] > len(titik_dilatasi):
            messagebox.showerror("Error Data", "Indeks garis di file garis.csv tidak valid.")
            return

        x1, y1, _ = titik_dilatasi[g[0] - 1][:3]
        x2, y2, _ = titik_dilatasi[g[1] - 1][:3]

        dda(canvas, x1, y1, x2, y2)

def animasi_rotasi():
    def rotasi_frame():
        nonlocal sudut
        global titik

        pivot = titik.mean(axis=0)[:3]  # Hitung pivot sebagai rata-rata koordinat
        translasi_ke_pivot = matriks_translasi(-pivot[0], -pivot[1], -pivot[2])
        translasi_kembali = matriks_translasi(pivot[0], pivot[1], pivot[2])
        rotasi = matriks_rotasi(sudut, 'z')

        matriks_akhir = np.dot(translasi_kembali, np.dot(rotasi, translasi_ke_pivot))
        titik = transformasi_3d(titik, matriks_akhir)

        gambar_garis()
        root.after(100, rotasi_frame)

    sudut = 5  # Sudut rotasi per frame dalam derajat
    rotasi_frame()

def flip_vertikal():
    global titik

    min_y = np.min(titik[:, 1])
    max_y = np.max(titik[:, 1])
    pivot_y = (min_y + max_y) / 2

    translasi_ke_pivot = matriks_translasi(0, -pivot_y, 0)
    translasi_kembali = matriks_translasi(0, pivot_y, 0)

    flip_matrix = np.array([
        [1, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    matriks_akhir = np.dot(translasi_kembali, np.dot(flip_matrix, translasi_ke_pivot))
    titik = transformasi_3d(titik, matriks_akhir)
    gambar_garis()

# Antarmuka Tkinter
root = tk.Tk()
root.title("Gambar Objek dengan Transformasi Matriks Homogen 3D")

frame = tk.Frame(root)
frame.pack(pady=10)

btn_gambar = tk.Button(frame, text="Gambar Objek", command=gambar_garis)
btn_gambar.pack(side=tk.LEFT, padx=5)

btn_rotasi = tk.Button(frame, text="Rotasi", command=animasi_rotasi)
btn_rotasi.pack(side=tk.LEFT, padx=5)

btn_flip = tk.Button(frame, text="Flip Vertikal", command=flip_vertikal)
btn_flip.pack(side=tk.LEFT, padx=5)

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack(pady=10)

# Baca file CSV
titik = baca_csv_titik("titik.csv")
garis = baca_csv_garis("garis.csv")

root.mainloop()
