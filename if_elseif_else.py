# Program Positif,Negatif,atau Nol?
# input nilai N (integer)

# KAMUS
# N : int

# ALGORITMA
N = int(input())

if N > 0 :
    output = 'positif'
elif N < 0:
    output = 'negatif'
else :   # N == 0
    output = 'nol'

print(output)