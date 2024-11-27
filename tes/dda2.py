import matplotlib.pyplot as plt
import random
import time

def draw_line_DDA(x1, y1, x2, y2):
    # Jika titik awal dan akhir sama, hanya tambahkan satu titik
    if x1 == x2 and y1 == y2:
        return [x1], [y1]

    # Menghitung dx dan dy
    dx = x2 - x1
    dy = y2 - y1

    # Menentukan jumlah langkah
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Menghitung perubahan x dan y di setiap langkah
    x_inc = dx / steps
    y_inc = dy / steps

    # Menyimpan titik awal
    x = x1
    y = y1

    # List untuk menyimpan semua titik garis
    x_points = [round(x)]
    y_points = [round(y)]

    # Menambahkan titik ke dalam list sebanyak jumlah langkah
    for _ in range(int(steps)):
        x += x_inc
        y += y_inc
        x_points.append(round(x))  # Pembulatan ke bilangan bulat
        y_points.append(round(y))

    return x_points, y_points

# Mengukur waktu mulai
start_time = time.time()

# Variabel untuk menyimpan semua titik
all_x_points = []
all_y_points = []

# Menghasilkan 1 juta garis dengan koordinat acak
num_lines = 1000000
for _ in range(num_lines):
    # Menghasilkan koordinat acak untuk setiap garis
    x1 = random.randint(0, 1000)
    y1 = random.randint(0, 1000)
    x2 = random.randint(0, 1000)
    y2 = random.randint(0, 1000)

    # Menggambar garis
    x_points, y_points = draw_line_DDA(x1, y1, x2, y2)
    all_x_points.extend(x_points)
    all_y_points.extend(y_points)

# Mengukur waktu selesai
end_time = time.time()
execution_time = end_time - start_time

# Visualisasi hanya sebagian dari titik untuk mencegah visualisasi berlebihan
sample_size = 1000  # Menampilkan hanya 1000 titik
sample_x_points = all_x_points[:sample_size]
sample_y_points = all_y_points[:sample_size]

# Gambar garis menggunakan Matplotlib
plt.plot(sample_x_points, sample_y_points, marker='o', markersize=2, linestyle='-', color="blue")
plt.title('Visualisasi Sampel 1 Juta Garis Acak (Algoritma DDA)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.axis('equal')
plt.show()

# Menampilkan waktu eksekusi
print(f"Waktu eksekusi untuk menggambar 1 juta garis acak: {execution_time:.2f} detik")
