S = "1001"

listS = list(map(int,S))
hasil = (2**3*listS[0]) + (2**2*listS[1]) + (2**1*listS[2]) + (2**0*listS[3])
print(hasil)