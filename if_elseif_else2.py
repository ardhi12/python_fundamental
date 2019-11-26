# Program WujudAir?
# input nilai suhu air (integer)

# KAMUS
# suhu air : float

# ALGORITMA
suhu = float(input())

if suhu <= 0 :
    output = 'beku'
elif suhu > 0 and suhu < 100 :
    output = 'cair'
else :  #suhu >= 100
    output = 'uap'

print(output)