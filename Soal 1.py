# Program KelulusanMahasiswa
# Menerima jumlah mahasiswa dan nilai tugas

# KAMUS
# jml_mhs, mhs_lulus, mhs_tidak_lulus,  : int

# ALGORITMA
mhs_lulus = 0
mhs_tidak_lulus = 0
count_mhs = 0
print("Range nilai tugas mata kuliah KU1072  : A , B , C , D , E , F")

jml_mhs = input('Masukan jumlah mahasiswa = ')

try:
    val = int(jml_mhs)     # cek apakah input berupa angka(integer)

    for i in range(1, val+1):
        nilai = input("Masukan nilai tugas mahasiswa ke-" + str(i) + " = ")
        count_mhs = count_mhs + 1

        if (nilai == 'A' or nilai == 'B' or nilai == 'C' or nilai == 'D'):
            mhs_lulus = mhs_lulus + 1
        elif (nilai == 'E' or nilai == 'F'):
            mhs_tidak_lulus = mhs_tidak_lulus + 1
        else:
            #do nothing
            print("Data yang dimasukan diluar dari range nilai!")
    print("")
    print("Jumlah mahasiswa yang lulus adalah = " + str(mhs_lulus))
    print("Jumlah mahasiswa yang tidak lulus adalah = " + str(mhs_tidak_lulus))
except ValueError:  #jika input bukan angka
    print("Input jumlah mahasiswa harus berupa angka!")