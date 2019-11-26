# global variable dapat diakses dari mana saja
# local varibale hanya dapat diakses dari dalam fungsinya saja

nama = 'ardhi'

def Namaku():
    # global nama                 # gunakan global untuk dapat merubah value dari variable global
    # nama = nama+' wayudhi'  
    nama = 'udin'                 # jika seperti ini maka variable nama dlm fungsi akan menjadi local variable
    print('dari dalam fungsi :', nama)

Namaku()
print('dari luar fungsi :', nama)