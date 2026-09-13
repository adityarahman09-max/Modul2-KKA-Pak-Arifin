import pandas as pd

# Membaca data yang sudah dibersihkan missing value-nya
df = pd.read_csv('/Users/adityarahman09/Documents/Moklet XI/KKA/Modul 2/data_kantin - data_kantin.csv')

print("--- Hasil Latihan 5 ---")
print("Jumlah data duplikat:", df.duplicated().sum())

# Menghapus duplikat
df = df.drop_duplicates()

# Mengubah tipe data harga menjadi integer
df['harga'] = df['harga'].astype(int)

print("\n=== Tipe Data Setelah Penyesuaian ===")
print(df.dtypes)

# Simpan dataset bersih akhir
df.to_csv('data_kantin_clean2.csv', index=False)