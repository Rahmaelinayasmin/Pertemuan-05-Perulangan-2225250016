# ============================================
# KUIS 2 - DERET ARITMETIKA
# Pertemuan 05 - Perulangan Python
# ============================================

print("Deret Aritmetika")

# Input suku pertama dan beda
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

# Input banyak suku
n = int(input("Banyak suku n: "))

# Validasi banyak suku
# Jika n tidak positif, input akan diminta kembali.
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

# Variabel untuk menyimpan jumlah seluruh suku
total = 0

# Menghasilkan n suku deret menggunakan for
for i in range(n):

    # Menghitung suku ke-(i + 1)
    suku = a + i * d

    # Menambahkan suku ke total
    total += suku

    # Menampilkan nomor dan nilai suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

# Menampilkan jumlah seluruh suku
print(f"Jumlah = {total:.2f}")