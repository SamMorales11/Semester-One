num = int(input("masukkan jumlah bilangan ganjil = "))

while num >= 2:
    if num % 2 == 1:
        print(num,end=" ")
    num -= 1

print(num)