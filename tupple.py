# tupples bersifat IMMUTABLE (permanen) / tidak bisa ditambah,edit,hapus
# bentuk dari tupples adalah kurung biasa ()

x = ('ardhi', 12, True)

print(x[2])
print(len(x))  # hitung jumlah value dlm tupples


y = ('ardhi', 'yudhi', 'wahyu')
print(max(y))  # max dilihat berdasarkan abjad dari huruf depan
print(min(y))  # min dilihat berdasarkan abjad dari huruf depan


# convert list -> tupple and tupple -> list #
z = ['nama', 'saya', 'adalah']

print(list(x)) 

print(tuple(z)) 