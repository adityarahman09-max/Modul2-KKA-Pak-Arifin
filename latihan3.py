import pandas as pd

# Pastikan file 'data_kantin.csv' berada di folder yang sama
df = pd.read_csv('/Users/adityarahman09/Documents/Moklet XI/KKA/Modul 2/data_kantin - data_kantin.csv')

print("--- Hasil Latihan 3 ---")
print("=== 5 Baris Pertama ===")
print(df.head())

print("\n=== Informasi Tipe Data & Missing Values ===")
print(df.info())

print("\n=== Ringkasan Statistik Numerik ===")
print(df.describe())

print("\n=== Ukuran Dataset (Baris, Kolom) ===")
print(df.shape)