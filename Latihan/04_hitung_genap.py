# ============================================
# LATIHAN 4 - MENGHITUNG BILANGAN GENAP
# Pertemuan 05 - Perulangan Python
# ============================================

# Input
n = int(input("n: "))

# Variabel untuk menghitung banyak bilangan genap
jumlah_genap = 0

# Perulangan dari 1 sampai n
for i in range(1, n + 1):

    # Mengecek apakah bilangan merupakan bilangan genap
    if i % 2 == 0:
        jumlah_genap += 1

# Output
print(f"Banyak bilangan genap = {jumlah_genap}")