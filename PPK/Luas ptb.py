import math

print("Menghitung Luas Permukaan Tabung")

r = 10 #jari jari tabung dalam cm
t = 40 #tinggi tabung dalam cm

pi = 22/7

luas_permukaan = 2 * math.pi * r * (r + t)

print(f"Luas permukaan tabung dengan jari-jari {r} cm dan tinggi {t} cm adalah {luas_permukaan:.2f} cm^2")