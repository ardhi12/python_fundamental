# Class dapat dipanggil dan diisi valuenya masing-masing.
class MyClass :
    # buat variable dan nilai default
    nama = ''
    umur = 0 

def MyFunc():
    saya = MyClass()            # buat variable dan panggil class
    saya.nama = 'Ardhi'         # isi value dari variable yang didalam class
    saya.umur = 22

    temen = MyClass()
    temen.nama = 'Temen'
    temen.umur = 12

    musuh = MyClass()
    
    print('nama saya adalah '+saya.nama+'. saya berumur '+ str(saya.umur)+' tahun')
    print('nama temen saya adalah '+temen.nama+'. saya berumur '+ str(temen.umur) +' tahun')
    print('nama musuh saya adalah '+musuh.nama+'. saya berumur '+ str(musuh.umur) +' tahun')

if __name__ == "__main__":
    MyFunc()

