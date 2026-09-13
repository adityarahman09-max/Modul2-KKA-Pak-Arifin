import pandas as pd

df = pd.read_csv('/Users/adityarahman09/Documents/Moklet XI/KKA/Modul 2/data_kantin - data_kantin.csv')

print("--- Hasil Latihan 4 ---")
print("=== Jumlah Missing Value Sebelum Cleaning ===")
print(df.isnull().sum())

# Clean missing value
df['terjual'] = df['terjual'].fillna(0) # Isi missing value terjual dengan 0
df = df.dropna(subset=['menu'])         # Hapus baris jika menu kosong

print("\n=== Jumlah Missing Value Setelah Cleaning ===")
print(df.isnull().sum())

# Simpan hasil sementara ke file baru
df.to_csv('data_kantin_clean1.csv', index=False)