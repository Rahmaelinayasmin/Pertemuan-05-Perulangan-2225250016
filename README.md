# Pertemuan 05 Perulangan Python

Nama: Rahma Elina Yasmin
NIM: 2225250016
Kelas: 3F

## Tujuan

Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan

Program dijalankan menggunakan Python 3 melalui terminal pada VS Code.

Perintah untuk menjalankan Kuis 2 Deret Aritmetika:

python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2

Langkah-langkah perulangan Kuis 2 Deret Aritmetika:

1. Memasukkan nilai suku pertama (a).
2. Memasukkan nilai beda (d).
3. Memasukkan banyak suku (n).
4. Memeriksa nilai n menggunakan perulangan while.
5. Jika n kurang dari atau sama dengan 0, program menampilkan pesan bahwa n harus bilangan bulat positif.
6. Memasukkan kembali nilai n sampai mendapatkan nilai yang valid.
7. Mengatur nilai total menjadi 0.
8. Menggunakan perulangan for sebanyak n kali.
9. Menghitung nilai suku dengan rumus suku = a + i * d.
10. Menambahkan nilai suku ke dalam total.
11. Menampilkan nomor dan nilai setiap suku.
12. Setelah perulangan selesai, menampilkan jumlah seluruh suku.

Menurut pemahaman saya, perulangan while digunakan untuk melakukan validasi terhadap nilai n. Jika nilai n belum valid, program akan terus meminta pengguna memasukkan nilai kembali. Perulangan for digunakan untuk menghasilkan setiap suku karena jumlah suku sudah diketahui dari nilai n.

## Hasil Pengujian

### Pengujian 1

Input:
a = 2
d = 3
n = 5

Keluaran yang diharapkan:
Suku ke-1: 2.00
Suku ke-2: 5.00
Suku ke-3: 8.00
Suku ke-4: 11.00
Suku ke-5: 14.00
Jumlah = 40.00

Keluaran aktual:
Suku ke-1: 2.00
Suku ke-2: 5.00
Suku ke-3: 8.00
Suku ke-4: 11.00
Suku ke-5: 14.00
Jumlah = 40.00

Status: Berhasil

### Pengujian 2

Input:
a = 10
d = -2
n = 4

Keluaran yang diharapkan:
Suku ke-1: 10.00
Suku ke-2: 8.00
Suku ke-3: 6.00
Suku ke-4: 4.00
Jumlah = 28.00

Keluaran aktual:
Suku ke-1: 10.00
Suku ke-2: 8.00
Suku ke-3: 6.00
Suku ke-4: 4.00
Jumlah = 28.00

Status: Berhasil

### Pengujian 3

Input:
a = 1.5
d = 0.5
n = 3

Keluaran yang diharapkan:
Suku ke-1: 1.50
Suku ke-2: 2.00
Suku ke-3: 2.50
Jumlah = 6.00

Keluaran aktual:
Suku ke-1: 1.50
Suku ke-2: 2.00
Suku ke-3: 2.50
Jumlah = 6.00

Status: Berhasil

## Refleksi

Salah satu kesalahan perulangan yang dapat terjadi adalah meletakkan total = 0 di dalam perulangan for. Jika total = 0 diletakkan di dalam perulangan, nilai total akan kembali menjadi 0 setiap kali perulangan berjalan sehingga jumlah seluruh suku tidak dapat dihitung dengan benar.

Cara memperbaikinya adalah meletakkan total = 0 sebelum perulangan for dimulai. Dengan begitu, nilai total dapat terus bertambah setiap kali satu suku dihitung.

Jumlah iterasi pada perulangan for ditentukan oleh nilai n. Jika n = 5, maka perulangan akan berjalan sebanyak 5 kali.

Variabel total harus diinisialisasi sebelum perulangan karena digunakan untuk menyimpan hasil penjumlahan setiap suku. Jika total = 0 diletakkan di dalam perulangan, hasil penjumlahan akan selalu dimulai kembali dari 0.

Validasi nilai n menggunakan while karena program perlu terus meminta input selama nilai n belum memenuhi syarat. Perulangan akan berhenti ketika pengguna memasukkan nilai n yang lebih dari 0.

Perulangan dapat dikatakan berhenti ketika kondisi while sudah tidak terpenuhi. Pada program ini, ketika n sudah lebih dari 0, kondisi n <= 0 menjadi salah sehingga perulangan while berhenti dan program melanjutkan proses berikutnya.