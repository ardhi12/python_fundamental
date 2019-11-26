# Silahkan input beberapa angka, lalu input -1 (agar whilenya false) untuk melihat hasilnya
N = int(input())
genap = 0
ganjil = 0


while (N >= 0) :
    # cek ganjil atau genap
    hasil_mod = N % 2  # persen (%) adalah modulo. modulo adalah sisa hasil bagi

    if hasil_mod == 0:
        genap = genap +1
    else:  # hasil_mod == 1
        ganjil = ganjil + 1
    N = int(input())

print("bilangan genap ada : " ,genap)
print("bilangan ganjil ada : " ,ganjil)