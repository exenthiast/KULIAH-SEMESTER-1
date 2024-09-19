a = input("Masukkan baris pertama: ").split()
b = input("Masukkan baris kedua: ").split()
print("\n")
c = input("Masukkan baris ketiga: ").split()
d = input("Masukkan baris keempat: ").split()

num1 = int(a[0])
num2 = int(a[1])
num3 = int(b[0])
num4 = int(b[1])

num5 = int(c[0])
num6 = int(c[1])
num7 = int(d[0])
num8 = int(d[1])

q = num1*num5 + num2*num7
w = num1*num6 + num2*num8
r = num3*num5 + num4*num7
t = num3*num6 + num4*num8

print("Perkalian hasil matriks tersebut adalah: ")
print(q, w)
print(r, t)