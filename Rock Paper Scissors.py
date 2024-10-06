import random

def main():
    """
    Permainan Batu-Kertas-Gunting di mana pemain bersaing dengan NPC.
    Peraturan Kemenangan:
    - Batu vs Kertas -> Kertas menang
    - Batu vs Gunting -> Batu menang
    - Kertas vs Gunting -> Gunting menang
    """
    cetak_peraturan_permainan()
    
    while True:
        pilihan_pemain = pilihan_pemain_user()
        pilihan_npc = random.randint(1, 3)

        # Paparkan pilihan
        nama_pilihan_pemain = dapatkan_nama_pilihan(pilihan_pemain)
        nama_pilihan_npc = dapatkan_nama_pilihan(pilihan_npc)

        print(f'Pilihan Anda = {nama_pilihan_pemain}')
        print('Giliran NPC -----')
        print(f'Pilihan NPC = {nama_pilihan_npc}')
        print('---------------------------\n')
        print('Keputusan = \n')

        # Tentukan keputusan
        tentukan_pemenang(pilihan_pemain, pilihan_npc)
        print('---------------------------\n')

        # Tanya jika pemain ingin main lagi
        if not main_lagi():
            break

def cetak_peraturan_permainan():
    """
    Cetak peraturan permainan Batu-Kertas-Gunting.
    """
    print('Peraturan Kemenangan:\n'
          '1. Batu vs Kertas -> Kertas menang\n'
          '2. Batu vs Gunting -> Batu menang\n'
          '3. Kertas vs Gunting -> Gunting menang\n')

def pilihan_pemain_user():
    """
    Meminta pemain memasukkan pilihan dan mengesahkannya.
    Pulangan:
        int: Pilihan pemain (1 untuk Batu, 2 untuk Kertas, 3 untuk Gunting)
    """
    print('Masukkan pilihan anda:\n 1 - Batu\n 2 - Kertas\n 3 - Gunting\n')
    while True:
        try:
            pilihan = int(input('Masukkan Pilihan Anda (1/2/3): '))
            if pilihan in [1, 2, 3]:
                return pilihan
            else:
                print('Pilihan tidak sah, sila masukkan 1, 2, atau 3.')
        except ValueError:
            print('Input tidak sah, sila masukkan nombor (1, 2, atau 3).')

def dapatkan_nama_pilihan(pilihan):
    """
    Mengembalikan nama berdasarkan pilihan pemain.
    
    Args:
        pilihan (int): Pilihan pemain atau NPC.
    
    Pulangan:
        str: Nama pilihan ('Batu', 'Kertas', atau 'Gunting').
    """
    if pilihan == 1:
        return 'Batu'
    elif pilihan == 2:
        return 'Kertas'
    elif pilihan == 3:
        return 'Gunting'

def tentukan_pemenang(pilihan_pemain, pilihan_npc):
    """
    Menentukan dan mencetak keputusan permainan antara pemain dan NPC.
    
    Args:
        pilihan_pemain (int): Pilihan pemain (1 untuk Batu, 2 untuk Kertas, 3 untuk Gunting).
        pilihan_npc (int): Pilihan NPC (1 untuk Batu, 2 untuk Kertas, 3 untuk Gunting).
    """
    if pilihan_pemain == pilihan_npc:
        print('Seri!')
    elif (pilihan_pemain == 1 and pilihan_npc == 3) or \
         (pilihan_pemain == 2 and pilihan_npc == 1) or \
         (pilihan_pemain == 3 and pilihan_npc == 2):
        print('Anda Menang!!!')
    else:
        print('NPC menang!')

def main_lagi():
    """
    Tanya pemain jika mereka ingin main lagi.
    
    Pulangan:
        bool: True jika pemain ingin main lagi, False jika tidak.
    """
    lagi = input("Main lagi? (y/n): ").strip().lower()
    return lagi == 'y'

if __name__ == "__main__":
    main()
