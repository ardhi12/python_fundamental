import time

print(' --- SELAMAT DATANG DI TAMAGOCHI ---')

nama = input('masukan nama monster : ')
stat = {'nama':nama, 'power':0}

def startGame():
    print('-- Main Menu --')
    print('1. Makan \n2. Bertarung \n3. Cek Status \n4. Exit Game')
    pilihan = input('Pilihan menu berdasarkan angka :')        
    if pilihan == '1':
        makan()
    elif pilihan == '2':
        bertarung()
    elif pilihan == '3':
        cekStatus()
    elif pilihan == '4':
        exitGame()
    else:
        print('Tidak ada dalam menu, silahkan pilih kembali')
        print()
        startGame()
    

def makan():
    print('nyam..nyam..')    
    print()
    stat['power'] += 50
    time.sleep(3)           # delay 3 detik
    startGame()    

def bertarung():
    print('ciaat..ciaaaat..')
    print()
    stat['power'] -= 10
    time.sleep(3)           # delay 3 detik
    startGame()

def cekStatus():
    print('cek..cek..')
    print(stat)
    print()
    time.sleep(3)           # delay 3 detik
    startGame()

def exitGame():
    print('bye..bye..') 
    print()   

startGame() 