# dictionary bentuknya adalah kurung kurawal {}
# isinya adalah key:value, mirip seperti json

x = {'nama' : 'ardhi',
     'umur' : 12,
     'WNI' : True,
    }

x['pekerjaan'] = 'Software Engineer'    # menambahkan value
x['WNI'] = False    # merubah value
del x['umur']       # menghapus key dan value

print(x)
print('namanya adalah ' + x['nama'])

for key, value in x.items():
    print(key + ' - ' + str(value))   # pakai convert str karena nilai True pada key WNI adalah boolean