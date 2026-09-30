# ============================================
# LATIHAN 1 - TABEL PERKALIAN
# Pertemuan 05 - Perulangan Python
# ============================================

# Input
n = int(input("Bilangan: "))

# Proses dan Output
# Menampilkan perkalian dari n x 1 sampai n x 10
for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")