import numpy as np

# Operasi Dasar NumPy Array
harga = np.array([5000, 7000, 3000, 12000, 4500])

print("--- Hasil Latihan 1 ---")
print('Rata-rata harga:', harga.mean())
print('Harga tertinggi:', harga.max())
print('Harga setelah diskon 10%:', harga * 0.9)