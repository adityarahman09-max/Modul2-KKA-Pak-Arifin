import pandas as pd

# Membuat DataFrame manual dengan missing value
data_kantin = {
    'menu': ['Nasi Goreng', 'Es Teh', 'Mie Ayam', 'Es Teh', None],
    'harga': [12000, 4000, 10000, 4000, 8000],
    'terjual': [23, 40, None, 35, 18]
}

df = pd.DataFrame(data_kantin)

print("--- Hasil Latihan 2 ---")
print(df)