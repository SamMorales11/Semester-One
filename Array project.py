# Membuat array kosong
numbers = []

# Meminta pengguna memasukkan bilangan
n = int(input("Masukkan banyaknya bilangan: "))
for i in range(n):
    num = float(input("Masukkan bilangan ke-{}: ".format(i+1)))
    numbers.append(num)

# Menghitung rata-rata
total = sum(numbers)
average = total / n

# Menampilkan hasil
print("Bilangan yang dimasukkan: ", numbers)
print("Rata-ratanya adalah: ", average)