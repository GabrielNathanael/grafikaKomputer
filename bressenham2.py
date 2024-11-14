import matplotlib.pyplot as plt
import random
import time

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    i1 = 2 * dy
    i2 = 2 * (dy - dx)
    d = i1 - dx

    if x1 > x2:
        x, y = x2, y2
        x_end = x1
    else:
        x, y = x1, y1
        x_end = x2

    x_points = [x]
    y_points = [y]

    while x < x_end:
        x += 1
        if d < 0:
            d += i1
        else:
            y += 1 if y1 < y2 else -1
            d += i2
        x_points.append(x)
        y_points.append(y)

    return x_points, y_points

# Mengukur waktu mulai
start_time = time.time()

# Variabel untuk menyimpan semua titik dari 1 juta garis
all_x_points = []
all_y_points = []

# Menghasilkan 1 juta garis dengan koordinat acak
num_lines = 1000
for _ in range(num_lines):
    x1 = random.randint(0, 100)
    y1 = random.randint(0, 100)
    x2 = random.randint(0, 100)
    y2 = random.randint(0, 100)
    
    # Pastikan x1, y1 dan x2, y2 tidak sama
    while x1 == x2 and y1 == y2:
        x2 = random.randint(0, 100)
        y2 = random.randint(0, 100)
    
    x_points, y_points = bresenham_line(x1, y1, x2, y2)
    all_x_points.extend(x_points)
    all_y_points.extend(y_points)

# Mengukur waktu selesai
end_time = time.time()
execution_time = end_time - start_time

# Visualisasi sebagian titik
sample_size = 1000  # Menggunakan sampel untuk visualisasi
sample_x_points = all_x_points[:sample_size]
sample_y_points = all_y_points[:sample_size]

plt.plot(sample_x_points, sample_y_points, marker='o', color="blue", markersize=2, linestyle='-')
plt.title("Visualisasi Sampel dari 1 Juta Garis dengan Koordinat Acak (Algoritma Bresenham)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis('equal')
plt.show()

# Tampilkan waktu eksekusi
print(f"Waktu eksekusi untuk menggambar 1 juta garis dengan koordinat acak: {execution_time:.2f} detik")
