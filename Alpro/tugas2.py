def  r(a) :
    match a :
        case "A"  | "B" :
            print("LULUS LANJUTKAN")
        case "C" :
            print("LULUS SEBAIKNYA DIULANG")
        case "D" :
            print("LULUS WAJIB DIULANG")
        case "E" :
            print("TIDAK LULUS")
a = input("masukkan nilai: ")
print (r(a))
