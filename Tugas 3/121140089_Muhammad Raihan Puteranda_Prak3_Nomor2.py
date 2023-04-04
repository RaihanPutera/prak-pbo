class AkunBank:
    # Untuk menampung data pelanggan
    list_pelanggan = []
    
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan.append(self)        # Menggabungkan data ke dalam list_pelanggan

    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        print(f"Halo {self.__nama_pelanggan}, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo {self.__jumlah_saldo}\n")
        self.lihat_menu()

    def tarik_tunai(self):
        jumlah_tarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))

        # Di ATM atau E-banking tidak bisa input negatif misal -10000 sehingga kode percabangan sebenarnya tidak perlu dibuat
        if (jumlah_tarik > 0):
            if (self.__jumlah_saldo > jumlah_tarik):
                self.__jumlah_saldo -= jumlah_tarik
                print("Saldo berhasil ditarik\n")
                self.lihat_menu()
            else:
                print("Nominal saldo yang anda punya tidak cukup!")
                self.tarik_tunai()
        else:
            print("Nominal tidak valid!")
            self.tarik_tunai()

    def transfer(self):
        ditemukan = False
        jumlah_transfer = int(input("Masukkan nominal yang ingin ditransfer: "))

        if (jumlah_transfer < 0):
            print("Nominal tidak valid!")
            self.transfer()
        else:
            no_rekening = int(input("Masukkan no rekening tujuan: "))

            # Mencari no rekening pelanggan yang tercatat di list_pelanggan
            for pelanggan in self.list_pelanggan:       
                if (no_rekening == pelanggan.__no_pelanggan):
                    ditemukan = True
                    if (self.__jumlah_saldo > jumlah_transfer):
                        self.__jumlah_saldo -= jumlah_transfer
                        pelanggan.__jumlah_saldo += jumlah_transfer
                        print(f"Transfer {jumlah_transfer} ke {pelanggan.__nama_pelanggan} sukses!\n")
                        self.lihat_menu()
                        break
                    else:
                        print("Nominal saldo yang anda punya tidak cukup!")
                        self.transfer()

            # Jika setelah pencarian, tak ditemukan no rekening pelanggan maka akan kembali ke menu utama
            if (ditemukan == False):            
                print("No rekening tujuan tidak dikenal! Kembali ke menu utama...\n")
                self.lihat_menu()

# main

Akun1 = AkunBank(1234, "Raihan", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.lihat_menu()
inputan = int(input("Masukkan nomor input: "))

while inputan != 4:
    if (inputan == 1):
        Akun1.lihat_saldo()
    elif (inputan == 2):
        Akun1.tarik_tunai()
    elif (inputan == 3):
        Akun1.transfer()
    else:
        print("Input tidak valid!")
    inputan = int(input("Masukkan nomor input: "))        

if (inputan == 4):
    exit()
