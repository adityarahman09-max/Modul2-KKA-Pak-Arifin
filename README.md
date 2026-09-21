# Modul2-KKA-Pak-Arifin

Tugas Analisis 1:
Hasil harga * 0.9 pada NumPy Array: Setiap elemen di dalam array langsung dikalikan dengan 0.9 (perhitungan otomatis ke seluruh elemen / vectorized operation). Hasilnya: [4500. 6300. 2700. 10800. 4050.].

Jika Menggunakan List Python [5000, 7000, 3000] * 0.9: Akan menghasilkan TypeError.

Penyebab Perbedaan: List Python biasa tidak mendukung operasi matematika langsung antar elemen. Pada list Python, perkalian hanya bisa dilakukan dengan bilangan bulat (integer) untuk mereplikasi/mengulang isi list (misal: [1, 2] * 2 menjadi [1, 2, 1, 2]). Sebaliknya, NumPy array dirancang khusus untuk komputasi numerik sehingga mendukung operasi matematika langsung (vectorized) tanpa perlu looping manual.

Tugas Analisis 2:
Kolom dengan Data Kosong:
- Kolom menu pada indeks ke-4 (bernilai None).  
- Kolom terjual pada indeks ke-2 (bernilai None / NaN).  

Risiko Langsung Menganalisis Data Tanpa Dibersihkan:
- Perhitungan Terdistorsi: Menghitung rata-rata terjual dapat menghasilkan nilai yang tidak akurat karena jumlah pembaginya berkurang atau bernilai salah.
- Error pada Operasi Aritmatika: Membuat kolom baru seperti total_pendapatan (harga * terjual) akan menghasilkan nilai NaN atau memicu error.
- Analisis Tidak Valid: Memiliki data penjualan tanpa nama menu membuat laporan bisnis tidak berguna karena kita tidak tahu transaksi tersebut milik produk apa.

Tugas Analisis 3:
Jawaban: Kolom yang jumlah non-null-nya lebih sedikit dari total baris (sesuai df.shape) menunjukkan adanya  missing value (data kosong) pada kolom tersebut.  

Artinya: Terdapat baris transaksi yang informasinya tidak lengkap pada kolom tersebut. Hal ini memberi petunjuk bahwa data tersebut memerlukan penanganan khusus (cleaning) sebelum masuk ke tahap analisis. 

Tugas Analisis 4:
Mengapa terjual Diisi (fillna(0)): Jika angka penjualan kosong, asumsi paling rasional adalah item tersebut tidak ada yang membeli (0 porsi terjual) pada periode itu. Mengisi dengan 0 menjaga keberadaan data menu tersebut tanpa merusak perhitungan total unit.  

Mengapa menu Kosong Dihapus (dropna): Kolom menu adalah entitas utama (identitas data). Data harga dan penjualan tanpa nama barang tidak dapat diidentifikasi dan tidak memberi nilai bisnis, sehingga lebih aman dihapus agar tidak mengotori analisis.  

Tugas Analisis 5:
Jumlah Baris Setelah drop_duplicates(): Jumlah baris berkurang sesuai dengan jumlah baris yang terdeteksi identik ganda.  
Pentingnya Memastikan Tipe Data (dtypes):  
- Kelancaran Operasi: Jika harga terbaca sebagai teks (string), operasi matematika seperti menghitung total omzet akan gagal atau menghasilkan pengulangan teks.
- Efisiensi Memori: Tipe data yang tepat (int/float) mempercepat kalkulasi Pandas dan meminimalkan konsumsi memori.  

Tugas Analisis 6:
Menu Pendapatan Tertinggi: Menu dengan omzet tertinggi ditentukan oleh perkalian antara harga jual dan volume unit terjual. (Misal: Nasi Goreng sering menghasilkan pendapatan tertinggi karena harganya lebih tinggi dari minuman, meskipun Es Teh terjual dalam kuantitas lebih banyak).  

Penerapan Pengambilan Keputusan Bisnis:  
- Manajemen Stok: Memastikan ketersediaan bahan baku menu utama agar tidak kehabisan stok (out of stock).
- Strategi Penjualan: Membuat paket hemat (bundling) antara menu berpendapatan tinggi dengan menu yang kurang laris.
- Evaluasi Menu: Mempertimbangkan efisiensi biaya atau penggantian menu jika ada produk yang penjualannya sangat rendah.

Analisis Proyek : 
6. Tahap yang Paling Menantang dan Cara Mengatasinya
Tahap Data Cleaning merupakan tahap yang paling menantang. Tantangan utamanya adalah menangani format data yang tidak konsisten pada kolom nilai (seperti adanya teks "poin" dan angka pencilan/outlier 999), serta menentukan penanganan missing value yang tepat tanpa merusak distribusi data.   Cara Mengatasinya: Kami menggunakan manipulasi string dan konversi numerik untuk membersihkan teks, mengganti nilai pencilan 999 menjadi missing value, lalu mengimputasinya menggunakan median agar tidak sensitif terhadap nilai ekstrem.   

7. Alasan Keputusan Membersihkan Data Harus Didasarkan Alasan yang Jelas
Keputusan data cleaning wajib didasari alasan rasional agar integritas dan validitas data tetap terjaga.   Jika data asal dibuang (drop), kita berisiko kehilangan informasi penting yang dapat mengurangi ukuran sampel.   Jika data diisi (fillna) secara asal-asalan, analisis agregat (seperti rata-rata dan standar deviasi) akan menjadi bias dan menghasilkan kesimpulan yang menyesatkan.

8. Hubungan Dataset Bersih dengan Pekerjaan Data Analyst di Dunia Nyata
Di dunia nyata, sekitar 70–80% waktu seorang Data Analyst dihabiskan untuk data cleaning dan preparation. Dataset bersih hasil dari proyek ini adalah pondasi utama sebelum memasuki tahap pembuatan dashboard, visualisasi data, hingga pengambilan keputusan bisnis (data-driven decision making). Tanpa data yang bersih (garbage in, garbage out), laporan atau rekomendasi analisis yang dihasilkan tidak akan dapat dipercaya oleh stakeholder.   
