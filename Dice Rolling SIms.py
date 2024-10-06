import random 

x = 'y'
while x == 'y':

    no = random.randint(1, 6)

    if no == 1:
        print('[-----]')
        print('[     ]')
        print('[  0  ]')
        print('[     ]')
        print('[-----]')
        
    if no == 2:
        print('[-----]')
        print('[ 0   ]')
        print('[     ]')
        print('[   0 ]')
        print('[-----]')   

    if no == 3:
        print('[-----]')
        print('[     ]')
        print('[0 0 0]')
        print('[     ]')
        print('[-----]')  
    
    if no == 4:
        print('[-----]')
        print('[0   0]')
        print('[     ]')
        print('[0   0]')
        print('[-----]')   

    if no == 5:
        print('[-----]')
        print('[0   0]')
        print('[  0  ]')
        print('[0   0]')
        print('[-----]')    

    if no == 6:
        print('[-----]')
        print('[0   0]')
        print('[0   0]')
        print('[0   0]')
        print('[-----]')    
    
    x = input ('press y to roll or n to exit = ')
    print('\n')

# Kod Python ini adalah simulasi lemparan dadu. Mari kita lihat secara terperinci bagaimana ia berfungsi:

# import random:

# Baris ini mengimport modul random, yang membolehkan kita menjana nombor rawak.
# x = 'y':

# Pembolehubah x diberikan nilai 'y' untuk memulakan gelung (while). Ini akan memastikan kod berjalan sekurang-kurangnya sekali.
# while x == 'y'::

# Gelung while ini akan terus berjalan selagi x adalah 'y'.
# Selepas setiap pusingan, pengguna akan ditanya jika mereka mahu melanjutkan lemparan dadu.
# no = random.randint(1, 6):

# random.randint(1, 6) menjana nombor rawak antara 1 hingga 6. Nilai ini disimpan dalam pembolehubah no.
# Ia mewakili nombor yang keluar dari lemparan dadu.
# if no == 1: hingga if no == 6::

# Ini adalah syarat untuk setiap nilai dadu (1 hingga 6).
# Bergantung kepada nilai no, corak dadu yang sepadan akan dicetak menggunakan simbol-simbol '[-----]', '[ 0 ]', dan sebagainya untuk mewakili titik pada dadu.