import random

num = int(input('Masukkan Jumlah Karakter Password = '))
while num > 0:
    print(chr((random.choice(range(33, 126)))),end=(''))
    num -= 1