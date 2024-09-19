def jenis_sudut(besar_sudut):
    if besar_sudut < 0 or besar_sudut > 180:
        return "Sudut tidak valid. Harus antara 0 dan 180 derajat."
    elif besar_sudut < 90:
        return "Sudut lancip (< 90 derajat)"
    elif besar_sudut == 90:
        return "Sudut siku-siku (= 90 derajat)"
    elif besar_sudut < 180:
        return "Sudut tumpul (> 90 derajat)"
    elif besar_sudut == 180:
        return "Sudut garis lurus (= 180 derajat)"

# Input dari pengguna
try:
    besar_sudut = float(input("Masukkan besar sudut dalam derajat: "))
    hasil = jenis_sudut(besar_sudut)
    print(hasil)
except ValueError:
    print("Input tidak valid. Masukkan angka yang valid untuk besar sudut.")
