# --- raise exception --- #

nama = 'ardhi'

# raise Exception("stop ada kesalahan")  

# print(i+nama)
# print('string ini tidak akan muncul karena ada kesalahan pada koding sebelumnya')



# --- try and except --- #
# try:
#     print(i+nama)
# except:                           # except juga dapat spesifik seperti "except NameError :", dapat dilihat di link hhtps://www.tutorialspoint.com/python/python_exceptions.htm
#     print('stop ada kesalahan')   # custom error message


# --- assert --- #
import sys

def apakah_linux():
    assert('linux' in sys.platform), "error! ternyata bukan linux"  

apakah_linux()
print('string ini tidak akan muncul karena ada kesalahan pada koding sebelumnya')

