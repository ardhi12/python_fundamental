# silahkan input beberapa angka, untuk melihat hasilnya silahkan input -999 (agar whilenya false)
N = int(input()) 
count = 0
sum = 0


while (N != -999) :
    count = count + 1
    sum = sum + N
    N = int(input())

if (count > 0 ):
    print("Banyaknya bilangnya yang masuk : " + str(count))  # str(count) jadi count dikonversi menjadi string
    print("Jumlah total  : " + str(sum))
    rata = sum/count
    print("Rata-rata  : " + str(rata))
else:
    print("Tidak ada data yang diolah")
