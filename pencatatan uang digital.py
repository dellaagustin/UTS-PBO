# Nama  : Della Agustin
# NIM   : 2007973
# Kelas : SIK B

saldo_umum = 0
saldo_tabungan = 0
pilihan = None
jumlah = None
penyimpanan = None

def menu () :
    global pilihan, jumlah, penyimpanan
    print("""
=== APLIKASI PENCATATAN UANG DIGITAL ===
[1] Informasi Saldo
[2] Tambah Saldo
[3] Ambil Saldo
[0] Keluar
=========================================
""")
def info_saldo () :
    print ('Saldo umum Anda saat ini adalah: Rp.{}'.format(saldo_umum),',-')
    print ('Saldo tabungan Anda saat ini adalah: Rp.{}'.format(saldo_tabungan),',-')

def tambah_saldo (tambah) :
    global saldo_umum, saldo_tabungan, penyimpanan

    if penyimpanan == 1:
        if tambah < 0:
            print('Penambahan saldo tidak dapat dilakukan!') 
        elif tambah > 0:
            saldo_umum = saldo_umum + tambah
            print ('Penambahan saldo sebesar Rp.{}'.format(tambah),',- berhasil!')
        print ('Saldo umum Anda saat ini adalah: Rp.{}'.format(saldo_umum),',-')
        print ('Saldo tabungan Anda saat ini adalah: Rp.{}'.format(saldo_tabungan),',-')

    elif penyimpanan == 2:
        if tambah < 0:
            print('Penambahan saldo tidak dapat dilakukan!') 
        elif tambah > 0:
            saldo_tabungan = saldo_tabungan + tambah
            print ('Penambahan saldo sebesar Rp.{}'.format(tambah),',- berhasil!')
        print ('Saldo umum Anda saat ini adalah: Rp.{}'.format(saldo_umum),',-')
        print ('Saldo tabungan Anda saat ini adalah: Rp.{}'.format(saldo_tabungan),',-')

def ambil_saldo (ambil) :
    global saldo_umum, saldo_tabungan, penyimpanan 

    if penyimpanan == 1:    
        if ambil <= saldo_umum:
            saldo_umum = saldo_umum - ambil
            print ('Pengambilan saldo sebesar Rp.{}'.format(ambil),',- berhasil!')
        elif ambil > saldo_umum:
            print('Pengambilan saldo tidak dapat dilakukan!') 
        print ('Saldo umum Anda saat ini adalah: Rp.{}'.format(saldo_umum),',-')
        print ('Saldo tabungan Anda saat ini adalah: Rp.{}'.format(saldo_tabungan),',-')

    elif penyimpanan == 2:       
        if ambil <= saldo_tabungan:
            saldo_tabungan = saldo_tabungan - ambil
            print ('Pengambilan saldo sebesar Rp.{}'.format(ambil),',- berhasil!')   
        elif ambil > saldo_tabungan:
            print('Pengambilan saldo tidak dapat dilakukan!') 
        print ('Saldo umum Anda saat ini adalah: Rp.{}'.format(saldo_umum),',-')
        print ('Saldo tabungan Anda saat ini adalah: Rp.{}'.format(saldo_tabungan),',-')
        
pilihan = None
jumlah = None
penyimpanan = None

while True:
    menu()
    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        info_saldo()
    elif pilihan == 2:
        print("""
[1] Umum
[2] Tabungan 
=========================================
""")
        penyimpanan = int(input("Pilih penyimpanan: "))
        jumlah = int(input("Nominal uang yang akan ditambahkan: "))
        tambah_saldo(jumlah)
    elif pilihan == 3:
        print("""
[1] Umum
[2] Tabungan 
=========================================
""")
        penyimpanan = int(input("Pilih penyimpanan: "))
        jumlah = int(input("Nominal uang yang akan diambil: "))
        ambil_saldo(jumlah)
    elif pilihan == 0:
        exit
        

