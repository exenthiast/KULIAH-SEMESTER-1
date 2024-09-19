import math

pi = 22/7

def luas_permukaan_tabung(radius, tinggi):
    luas = 2 * math.pi * radius * (radius + tinggi)
    return luas

radius = float(input("Masukkan  jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

luas_permukaan = luas_permukaan_tabung(radius, tinggi)

print(f"Luas Permukaan Tabung adalah: {luas_permukaan:.2f} cm^2")