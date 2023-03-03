class data_diri:
    # Konstruktor
    def __init__(self, nama, nim, kelas_pbo, jumlah_sks, umur):
        self.nama = nama
        self.nim = nim
        self.__kelas_pbo = kelas_pbo    # Private karena tidak bisa sembarang diganti
        self.jumlah_sks = jumlah_sks
        self.umur = umur
        self.uang = 0
        
    # Method
    def tambah_uang(self, tambah):
        self.uang += tambah
        print(f"Uang  {tambah} telah ditambah!")

    @property                     # Ambil atribut self.__kelas_pbo yang bersifat private
    def kelas_pbo(self):
        return self.__kelas_pbo
                                    
    @kelas_pbo.setter             # Tetapkan kelas saat ini
    def kelas_pbo(self, kelas):
        self.__kelas_pbo = kelas

# main

# Data diri bisa lewat input atau sudah ditulis kode sebelumnya
inputan = str(input("Apakah anda ingin menginput nama sendiri? y/n "))

while (inputan.lower() != "y") and (inputan.lower() != "n"):
    print("Input tidak valid, silahkan coba lagi!")
    inputan = str(input())
    
if (inputan.lower() == "y"):
    nama = str(input("Masukkan nama: "))
    nim = int(input("Masukkan NIM: "))
    kelas_pbo = str(input("Masukkan kelas pbo: "))
    jumlah_sks = int(input("Masukkan jumlah SKS: "))
    umur = int(input("Masukkan umur: "))
    
    mhs1 = data_diri(nama, nim, kelas_pbo, jumlah_sks, umur)
    
elif (inputan.lower() == "n"):
    mhs1 = data_diri("Raihan", "121140089", "RB", 20, 19)
    
print(f"\n{mhs1.__dict__}")     # Menampilkan seluruh atribut dari objek

# Contoh penggunaan
aksi = int(input("Apa yang mau dilakukan? (1). Tambah uang (2). Ganti Kelas "))
while (aksi == 1) or (aksi == 2):
    if (aksi == 1):
        tambah = int(input("Masukkan jumlah uang yang akan ditambah: "))
        mhs1.tambah_uang(tambah)
        print(f"Uang yang dimiliki: {mhs1.uang}\n")

    elif (aksi == 2):
        print(f"Kelas sebelumnya: {mhs1.kelas_pbo}")
        kelas = str(input("Masukkan kelas yang diinginkan: "))
        mhs1.kelas_pbo = kelas
        print(f"Kelas setelah pindah: {mhs1.kelas_pbo}\n")
        
    else:
        exit()
    
    aksi = int(input("Apa yang mau dilakukan? (1). Tambah uang (2). Ganti Kelas ")) 
