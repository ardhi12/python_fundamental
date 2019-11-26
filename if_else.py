# Program GenapatauGanjil
# input nilai N (integer)

# KAMUS
# N : int

# ALGORITMA
N = int(input())
hasil_mod = N % 2      # persen (%) adalah modulo. modulo adalah sisa hasil bagi

if hasil_mod == 0 :
    output = 'genap'
else:  # hasil_mod == 1
    output = 'ganjil'

print(output)