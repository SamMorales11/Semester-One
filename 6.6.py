# Python program untuk mencari persamaan akar kuadrat No 3
import math

# fungsi mencari persamaan akar
def persamaan_akar( a, b, c):

    # rumus persamaan kuadrat
    D = b * b - 4 * a * c
    akar_d = math.sqrt(abs(D))

    # eksekusi kondisional
    if D > 0:
        print("(-b+√d)/2a\n",(-b + akar_d)/(2 * a))
        print("(-b+√d)/2a\n",(-b - akar_d)/(2 * a))
    elif D == 0:
        print("(-b/2a\n",-b / (2 * a))                      
    else:1
print("akar imaginer")  

    #  deklarasi
print("D = b²-4ac\nmasukkan a b c")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

# If a is 0, then incorrect equation
if a == 0:
        print("a tidak boleh = 0")
else:
    persamaan_akar(a, b, c)