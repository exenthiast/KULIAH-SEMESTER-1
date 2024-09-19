import math

pi = 22/7

def volume_kerucut(radius, tinggi):
    volume = 1/3 * (math.pi*radius*radius*tinggi)
    return volume

radius = float(input("Masukkan  jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))

volume_kerucut = volume_kerucut(radius, tinggi)

print(f"Luas Permukaan Tabung adalah: {volume_kerucut:.2f} cm^2")