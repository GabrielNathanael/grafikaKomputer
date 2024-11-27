import matplotlib.pyplot as plt
import random
import time  

def draw_line(x1, y1, x2, y2):
    x_points = []
    y_points = []

    # Pastikan x1 <= x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1  # Tukar y juga jika x ditukar

    # Hitung gradien
    m = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')

    # Jika garis vertikal
    if x1 == x2:
        y = y1
        while y <= y2:
            x_points.append(x1)
            y_points.append(y)
            y += 1
        return x_points, y_points

    # Jika garis horizontal
    elif y1 == y2:
        x = x1
        while x <= x2:
            x_points.append(x)
            y_points.append(y1)
            x += 1
        return x_points, y_points

    # Jika gradien lebih dari 1, iterasi melalui y
    if abs(m) > 1:
        if y1 > y2:  # Pastikan kita iterasi dari y1 ke y2
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            x = x1 + (y - y1) / m
            x_points.append(round(x))  # Pembulatan untuk pixel
            y_points.append(y)
    else:  # Jika gradien kurang dari 1, iterasi melalui x
        for x in range(x1, x2 + 1):
            y = y1 + m * (x - x1)
            y_points.append(round(y))  # Pembulatan untuk pixel
            x_points.append(x)

    return x_points, y_points

# Menggambar 1 juta garis dengan koordinat acak
num_lines = 1000000
all_x_points = []
all_y_points = []

# Mengukur waktu mulai
start_time = time.time()

for _ in range(num_lines):
    # Menghasilkan koordinat acak
    x1 = random.randint(0, 100)
    y1 = random.randint(0, 100)
    x2 = random.randint(0, 100)
    y2 = random.randint(0, 100)

    # Menggambar garis
    x_points, y_points = draw_line(x1, y1, x2, y2)
    all_x_points.extend(x_points)
    all_y_points.extend(y_points)

# Mengukur waktu selesai
end_time = time.time()
execution_time = end_time - start_time

# Visualisasi hanya sebagian dari titik
sample_size = 1000  # Jumlah titik yang ingin ditampilkan
sample_indices = random.sample(range(len(all_x_points)), sample_size)

# Mengambil sampel titik untuk visualisasi
sample_x_points = [all_x_points[i] for i in sample_indices]
sample_y_points = [all_y_points[i] for i in sample_indices]

# Gambar garis menggunakan Matplotlib
plt.plot(sample_x_points, sample_y_points, marker='o', linestyle='-', markersize=1)
plt.title('1 Juta Garis dengan Koordinat Acak')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.axis('equal')
plt.show()

# Menampilkan waktu eksekusi
print(f"Waktu eksekusi: {execution_time:.2f} detik")
