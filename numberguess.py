import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = int(input("Guess a number between 1 and 10: "))
    guess = int(guess)
    
    if guess == num :
        print('You Right, You Won!!!')
        break
    else:
        print('Wrong, Try Again')


# Penjelasan:

# import random - Baris ini mengimport modul random yang membolehkan kita menggunakan fungsi rawak.

# num = random.randint(1, 10) - Baris ini menghasilkan nombor rawak antara 1 dan 10 dan menyimpannya dalam pembolehubah num.

# guess = None - Pembolehubah guess diisytiharkan dengan nilai awal None. Ini bermaksud ia belum mempunyai nilai.

# while guess != num: - Ini adalah gelung while yang akan terus berjalan selagi tekaan (guess) tidak sama dengan nombor rawak (num).

# guess = int(input("Guess a number between 1 and 10: ")) - Dalam gelung while, pengguna akan diminta untuk meneka nombor antara 1 hingga 10. Fungsi input() digunakan untuk mendapatkan input dari pengguna, dan int() digunakan untuk menukar input tersebut kepada nombor bulat.

# if guess == num : - Bahagian ini memeriksa jika tekaan pengguna (guess) adalah sama dengan nombor rawak (num).

# print('You Right, You Won!!!') - Jika betul, program akan mencetak "You Right, You Won!!!" dan kemudian menghentikan gelung menggunakan break.
# else: - Jika tekaan pengguna tidak betul:

# print('Wrong, Try Again') - Program akan mencetak "Wrong, Try Again" dan meminta pengguna meneka semula.
# Tujuan Kod: Kod ini adalah satu permainan yang meminta pengguna meneka nombor antara 1 hingga 10 sehingga mereka 
# meneka dengan betul. Jika pengguna berjaya, program akan menghentikan permainan dan mencetak mesej kemenangan.