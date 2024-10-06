numlist = list()

while True:
    inp = input ('masukkan nombor = ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist)/ len(numlist)
print('Purata = ', average)


# ```

# **Penjelasan:**
# 1. **numlist = list()** - Baris ini mencipta senarai kosong yang dipanggil `numlist`. Ia akan digunakan untuk menyimpan nombor yang dimasukkan oleh pengguna.

# 2. **while True:** - Ini adalah gelung `while` yang akan berterusan (`True`), bermaksud ia akan berjalan sampai kita menghentikannya menggunakan `break`.

# 3. **inp = input('masukkan nombor = ')** - Dalam gelung ini, pengguna diminta memasukkan nombor. Mesej "masukkan nombor =" akan dipaparkan, dan input pengguna akan disimpan dalam pembolehubah `inp`.

# 4. **if inp == 'done': break** - Jika pengguna memasukkan `done`, gelung akan dihentikan menggunakan `break`. Ini adalah cara untuk pengguna memberitahu bahawa mereka sudah selesai memasukkan nombor.

# 5. **value = float(inp)** - Input pengguna ditukar kepada jenis nombor perpuluhan (`float`) dan disimpan dalam `value`.

# 6. **numlist.append(value)** - Nilai `value` kemudian dimasukkan ke dalam senarai `numlist` menggunakan `append()`.

# 7. **average = sum(numlist) / len(numlist)** - Selepas pengguna selesai memasukkan nombor, purata dikira. `sum(numlist)` mengira jumlah keseluruhan semua nombor dalam senarai, manakala `len(numlist)` memberikan bilangan elemen dalam senarai. Purata diperoleh dengan membahagikan jumlah dengan bilangan elemen.

# 8. **print('Purata = ', average)** - Akhirnya, purata yang dikira akan dicetak dengan mesej "Purata = " diikuti dengan nilai purata.

# **Tujuan Kod:**
# Kod ini membolehkan pengguna memasukkan beberapa nombor dan kemudian menghitung purata nombor-nombor tersebut. Pengguna boleh memasukkan `done` apabila mereka selesai memasukkan nombor, dan program akan mengira dan mencetak purata.