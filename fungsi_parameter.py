# fungsi dapat tidak memiliki parameter atau bahkan lebih dari 1 parameter
# nilai default parameter dapat di isi pada fungsi

def kenalan(nama = 'kosong',umur='belum diisi'):
    print('halo, nama saya ' + nama + ". saya berumur " + str(umur) + " tahun")

kenalan('ardhi',12)
kenalan(umur= 27, nama='udin')     # ini adalah keyword argumen, jadi keywordnya dimasukan jg ke dalam argumen. walupun urutannya salah, tetapi tetap hasilnya benar.
kenalan()               # ketika user lupa memasukan parameter, maka nilai defaultnya yang akan masuk
print()

def hitung(a=1, b=2):  
    return a+b          # untuk mengembalikan nilai/hasil

print(hitung(2,3))

