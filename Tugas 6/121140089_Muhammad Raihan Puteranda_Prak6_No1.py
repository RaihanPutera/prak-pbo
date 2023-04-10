from abc import ABC, abstractmethod     # Import kelas ABC dan decorator fungsi abstrak

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo

    # Fungsi konkrit    
    def lihat_saldo(self):
        print(f"Saldo saat ini {self.saldo}")

    # Fungsi abstrak    
    @abstractmethod
    def transfer_saldo(self, transfer):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        self.biaya_administrasi = 0
        self.usia_akun = 2023 - self.tahun_daftar
        self.suku_bunga = 0
    
    # Implementasi fungsi abstrak transfer_saldo
    def transfer_saldo(self, transfer):
        self.usia_akun = 2023 - self.tahun_daftar
        if (self.usia_akun >= 3 and transfer >= 100000):
            self.biaya_administrasi = 0
            self.saldo = self.saldo - (transfer + self.biaya_administrasi)
            print(f"Saldo berjumlah {transfer} berhasil ditransfer dengan biaya admin {self.biaya_administrasi}")
        elif (self.usia_akun < 3 and transfer >= 100000):
            self.biaya_administrasi = 2000
            self.saldo = self.saldo - (transfer + self.biaya_administrasi)
            print(f"Saldo berjumlah {transfer} berhasil ditransfer dengan biaya admin {self.biaya_administrasi}")
        elif (transfer < 100000):
            self.biaya_administrasi = 0
            self.saldo = self.saldo - (transfer + self.biaya_administrasi)
            print(f"Saldo berjumlah {transfer} berhasil ditransfer dengan biaya admin {self.biaya_administrasi}")
    
    # Implementasi fungsi abstrak lihat_suku_bunga
    def lihat_suku_bunga(self):
        self.usia_akun = 2023 - self.tahun_daftar
        if (self.usia_akun >= 3 and self.saldo >= 1000000000):
            self.suku_bunga = "1%"
            print(f"Suku bunga per-bulan: {self.suku_bunga}")
        elif (self.usia_akun < 3 and self.saldo >= 1000000000):
            self.suku_bunga = "2%"
            print(f"Suku bunga per-bulan: {self.suku_bunga}")
        elif (self.saldo < 1000000000):
            self.suku_bunga = "3%"
            print(f"Suku bunga per-bulan: {self.suku_bunga}")

class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        self.biaya_administrasi = 0
        self.usia_akun = 2023 - self.tahun_daftar
        self.suku_bunga = 0
    
    # Implementasi fungsi abstrak transfer_saldo
    def transfer_saldo(self, transfer):
        if (self.usia_akun >= 3 and transfer >= 100000):
            self.biaya_administrasi = 2000
            self.saldo = self.saldo - (transfer + self.biaya_administrasi)
            print(f"Saldo berjumlah {transfer} berhasil ditransfer dengan biaya admin {self.biaya_administrasi}")
        elif (self.usia_akun < 3 and transfer >= 100000):
            self.biaya_administrasi = 5000
            self.saldo = self.saldo - (transfer + self.biaya_administrasi)
            print(f"Saldo berjumlah {transfer} berhasil ditransfer dengan biaya admin {self.biaya_administrasi}")
        elif (transfer < 100000):
            self.biaya_administrasi = 0
            self.saldo = self.saldo - (transfer + self.biaya_administrasi)
            print(f"Saldo berjumlah {transfer} berhasil ditransfer dengan biaya admin {self.biaya_administrasi}")
    
    # Implementasi fungsi abstrak lihat_suku_bunga
    def lihat_suku_bunga(self):
        if (self.usia_akun >= 3 and self.saldo >= 10000000):
            self.suku_bunga = "1%"
            print(f"Suku bunga per-bulan: {self.suku_bunga}")
        elif (self.usia_akun < 3 and self.saldo >= 10000000):
            self.suku_bunga = "2%"
            print(f"Suku bunga per-bulan: {self.suku_bunga}")
        elif (self.saldo < 10000000):
            self.suku_bunga = "3%"
            print(f"Suku bunga per-bulan: {self.suku_bunga}")
            
# main

akun1 = AkunGold("Raihan", 2019, 1500000000)
akun2 = AkunSilver("Putera", 2021, 12000000)
akun1.lihat_saldo()
akun1.transfer_saldo(300000)
akun1.lihat_saldo()
akun1.lihat_suku_bunga()
akun2.lihat_saldo()
akun2.transfer_saldo(300000)
akun2.lihat_saldo()
akun2.lihat_suku_bunga()
