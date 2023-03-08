"""
 Misalkan ada 3 buah kasta yakni rakyat, pemerintah, dan presiden. Masing-masing memiliki harta yang tingkat keamanannya
 berbeda-beda
"""
class rakyat:
    # Public Access Modifier yang bisa diakses diluar kelasnya termasuk kelas lain
    def __init__(self, nama, harta):
        self.nama = nama
        self.harta = harta

    def ambil_harta(self, ambil):
        self.harta -= ambil
        print(f"Harta berjumlah {ambil} telah diambil")
        print(f"Jumlah harta rakyat saat ini: {self.harta}\n")   

    # Masih bisa diambil karena python tidak benar-benar mempunyai access modifier "protected"
    def ambil_harta_pemerintah(self, ambil):                            
        pemerintah._harta -= ambil                                      # Anggap saja sebagai bantuan dana (BPJS)
        print(f"Pemerintah telah meminjamkan {ambil} kepada rakyat\n")

    # Tak bisa mengambil karena hanya presiden yang memegang hartanya (Private)
    def ambil_harta_presiden(self, ambil):          
        presiden.__harta_personal -= ambil

    def info_harta(self):
        print(f"Harta rakyat saat ini: {self.harta}\n")    

class pemerintah:
    # Python tidak benar-benar memiliki "Protected Access Modifier" oleh karena itu masih bisa diakses dari luar kelas & subclassnya
    def __init__(self, nama, harta):
        self.nama = nama
        self._harta = harta

    """
        @property
        def harta(self):            # Bisa menggunakan decorator/set-getter untuk membuat self._harta protected
            return self._harta

        @harta.setter
        def harta(self, harta):
            self._harta = harta    
    """            

    def ambil_harta(self, ambil):
        if (self._harta > 0):
            self._harta -= ambil
            print(f"Harta berjumlah {ambil} telah diambil")
            print(f"Jumlah harta pemerintah saat ini: {self._harta}\n")
        else:
            print("Pemerintah telah bangkrut!\n")    

    # Fungsi protected juga masih bisa diakses diluar kelas
    def _ambil_harta_rakyat(self, ambil):
        if (rakyat.harta > 0):                     
            rakyat.harta -= ambil                           # Mengakses harta rakyat untuk diambil karena sifatnya yang public
            self._harta += ambil                           
            print(f"Pemerintah telah mengkorupsi sejumlah {ambil} dari harta rakyat")
            print(f"Jumlah harta rakyat saat ini: {rakyat.harta}\n")
        else:
            print("Rakyat sudah jatuh miskin!\n")

    def info_harta(self):
        print(f"Harta pemerintah saat ini: {self._harta}\n")            

# Anggap presiden sebagai subclass pemerintah agar bisa mengakses hartanya
class presiden(pemerintah):                             
    # Private Access Modifier hanya bisa diakses di kelasnya sendiri
    def __init__(self, nama, harta, harta_personal):
        super().__init__(nama, harta)                   
        self.__harta_personal = harta_personal
    
    def ambil_harta_presiden(self, ambil):
            if (self.__harta_personal > 0):
                self.__harta_personal -= ambil
                print(f"Harta berjumlah {ambil} telah diambil")
                print(f"Jumlah harta presiden saat ini: {self.__harta_personal}\n")
            else:
                print("Harta habis!\n")        

    # Fungsi private dapat diakses dengan membuat method "get" baru untuk bisa memanggilnya
    def __kosongkan_harta_presiden(self):
        self.__harta_personal = 0

    def kosong_harta(self):                 
        self.__kosongkan_harta_presiden()    

    # Dikarenakan presiden subclass pemerintah, maka bisa mengakses atributnya
    def ambil_harta_pemerintah(self, ambil):    
        if (pemerintah._harta > 0):
            pemerintah._harta -= ambil
            self._harta -= ambil
            self.__harta_personal += ambil
            print(f"Presiden telah mengambil simpanan sejumlah {ambil} dari harta pemerintah")
            print(f"Jumlah harta pemerintah saat ini: {pemerintah._harta}\n")
        else:
            print("Harta pemerintah sudah terkuras!\n")

    def info_harta(self):
        print(f"Harta presiden saat ini: {self.__harta_personal}\n")            
   

# main

rakyat = rakyat("Gill Bates", 1000000000)
pemerintah = pemerintah("Donal D Rump", 5000000000)
presiden = presiden("Joe Biedan", 5000000000, 10000000000)

rakyat.ambil_harta(500000)
# rakyat.ambil_harta_presiden(4000)      akan terjadi error karena harta presiden bersifat private
rakyat.ambil_harta_pemerintah(5000)
rakyat.info_harta()     
presiden.ambil_harta_pemerintah(2000)
presiden.info_harta()
pemerintah._ambil_harta_rakyat(2000)
pemerintah.info_harta()

"""
    Penjelasan demonstrasi:
    Ibarat rakyat memiliki sebuah uang/harta yang disimpan di suatu instansi, uang tersebut bisa diakses oleh instansi tersebut,
    dalam demonstrasi ini anggap instansi tersebut sebagai pemerintah. Untuk harta pemerintah sendiri tentu dilindungi dan tidak bisa
    sembarang diambil oleh rakyat (kecuali sebagai bantuan) tapi bisa diambil oleh suatu kuasa yang lebih tinggi yaitu misal presiden.
    Harta personal presiden dan wewenangnya (fungsi) sendiri hanya bisa diakses oleh presiden itu sendiri dan tidak bisa diakses oleh 
    siapapun termasuk pemerintah. Sehingga dapat diibaratkan: Rakyat (Public), Pemerintah (Protected), Presiden (Private)
"""

""" 
    Kesimpulannya, penggunaan Access Modifier tergantung proyek yang akan dibuat, jika ingin suatu kelas / atribut yang dapat diakses semua
    bagian diluar kelas dapat menggunakan Public, sedangkan jika ingin ada suatu kelas / atribut yang hanya dibatasi untuk beberapa bagian
    saja / ruang lingkupnya kecil maka bisa menggunakan Protected (untuk pewarisan) atau Private.
"""


