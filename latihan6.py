import pandas as pd

# Membaca data yang sudah bersih total dari Latihan 5
df = pd.read_csv('/Users/adityarahman09/Documents/Moklet XI/KKA/Modul 2/data_kantin - data_kantin.csv')

print("--- Hasil Latihan 6 ---")

# 1. Filtering: Menu laris (terjual > 20)
laris = df[df['terjual'] > 20]
print("=== Menu Laris (>20 porsi) ===")
print(laris)

# 2. Sorting: Mengurutkan dari penjualan terbanyak
urut = df.sort_values(by='terjual', ascending=False)
print("\n=== Urutan Penjualan Terbanyak ===")
print(urut)

# 3. Kolom Turunan: Total Pendapatan
df['total_pendapatan'] = df['harga'] * df['terjual']

# 4. Groupby & Agregasi: Total pendapatan per menu
ringkasan = df.groupby('menu')['total_pendapatan'].sum()
print("\n=== Ringkasan Total Pendapatan Per Menu ===")
print(ringkasan)

# Simpan file final untuk proyek/visualisasi selanjutnya
df.to_csv('dataset_bersih.csv', index=False)