num = int(input("masukkan nilai factorial = "))
result = 0
factorial = 1

print(f"{num}! = ",end="")

while result < num - 1:
    result += 1
    print(result,end=" x ")

result += 1
print(result,end=" = ")

while num > 0:
    factorial *= num
    num -= 1
print(factorial)