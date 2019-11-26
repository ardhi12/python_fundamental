# Program BeratAtlit
# Menerima berat badan atlit

# KAMUS
# bb : int
# kelas : str

# ALGORITMA
print("-- Range Berat Badan --")
print("45 - 50 Kg : Kelas A")
print("51 - 55 Kg : Kelas B")
print("56 - 60 Kg : Kelas C")
print("61 - 65 Kg : Kelas D")
print("66 - 70 Kg : Kelas E")
print("< 70 Kg : Kelas F")
print("> 45 Kg : Tidak memenuhi kualifikasi")
print("")

bb = input("Masukan berat badan atlit : ") #input berat badan

try:
    val = int(bb)       # cek apakah input berupa angka(integer)

    #Range Berat Badan
    if val >= 45 and val <= 50:
        kelas = "Atlit berada pada kelas A"
    elif val > 50 and val <= 55:
        kelas = "Atlit berada pada kelas B"
    elif val > 55 and val <= 60:
        kelas = "Atlit berada pada kelas C"
    elif val > 60 and val <= 65:
        kelas = "Atlit berada pada kelas D"
    elif val > 65 and val <= 70:
        kelas = "Atlit berada pada kelas E"
    elif val > 70:
        kelas = "Atlit berada pada kelas F"
    else:  # bb < 45
        kelas = "Tidak memenuhi kualifikasi"

    print(kelas);

except ValueError:  #jika input bukan angka
    print("Input data harus berupa angka!")