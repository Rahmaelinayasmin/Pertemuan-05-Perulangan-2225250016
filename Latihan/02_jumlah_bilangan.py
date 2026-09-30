# ============================================
# LATIHAN 2 - JUMLAH BILANGAN
# Pertemuan 05 - Perulangan Python
# ============================================

# Input
n = int(input("n: "))

# Proses
# total dimulai dari 0 sebelum perulangan
total = 0

# Menjumlahkan bilangan dari 1 sampai n
for i in range(1, n + 1):
    total += i

# Output
print(f"Jumlah = {total}")