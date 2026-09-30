# ============================================
# LATIHAN 3 - VALIDASI INPUT
# Pertemuan 05 - Perulangan Python
# ============================================

# Input awal
nilai = float(input("Nilai 0-100: "))

# Validasi menggunakan while
# Program akan terus meminta input selama nilai
# berada di luar rentang 0 sampai 100.
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

# Output
print(f"Nilai diterima: {nilai}")