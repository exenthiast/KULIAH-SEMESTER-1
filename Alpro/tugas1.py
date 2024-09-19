x = input("Nilai mata Kuliah: ")

"A" == 90
"B" == 80
"C" == 70
"D" == 60
"E" == 50

if x == "A" or x == "B" :
    predikat = ("LULUS dan LANJUTKAN")
elif x == "C" :
    predikat = ("LULUS SEBAIKNYA DIULANGI")
elif x == "D" :
    predikat = ("LULUS WAJIB DIULANGI")
elif x == "E" :
    predikat =("TIDAK LULUS")
else: "nilai tidak valid"

print(predikat)
