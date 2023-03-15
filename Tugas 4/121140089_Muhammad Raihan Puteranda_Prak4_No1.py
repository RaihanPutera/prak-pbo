# Parent class
class Komputer:
    def __init__(self, nama ,jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

# Child class    
class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        super().__init__(nama, jenis, harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor
    
class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas

class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas, rpm):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas
        self.rpm = rpm

class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas

class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya):
        super().__init__(nama, jenis, harga, merk)
        self.daya = daya

# main

# Menampung list pc rakitan yang ada
rakit = []

# Di soal kekurangan atribut "jenis" sehingga ditambahkan dan ada perbaikan
p1 = Processor('Core i7 7740X','Processor', 4350000, 'Intel', 4, '4.3GHz')
ram1 = RAM('DDR4 SODimm PC19200/2400MHz', 'RAM', 328000, 'V-Gen', '4GB')
hdd1 = HDD('HDD 2.5 inch', 'HDD', 295000, 'Seagate', '500GB', 7200)
vga1 = VGA('GTX 1050', 'VGA', 250000, 'Asus', '2GB')
psu1 = PSU('Corsair V550', 'PSU', 250000, 'Corsair', '500W')

# Menggabungkan ke dalam list
rakit.append([p1, ram1, hdd1, vga1, psu1])

p2 = Processor('Ryzen 5 3600', 'Processor', 250000, 'AMD', 4, '4.3GHz')
ram2 = RAM('DDR4 2400MHz', 'RAM', 328000, 'G.SKILL', '4GB')
hdd2 = HDD('HDD 2.5 inch', 'HDD', 295000, 'Seagate', '1000GB', 7200)
vga2 = VGA('GTX 1060Ti', 'VGA', 250000, 'Asus', '8GB')
psu2 = PSU('Corsair V550', 'PSU', 250000, 'Corsair', '500W')

rakit.append([p2, ram2, hdd2, vga2, psu2])

# Enumerate untuk membaca list satu-satu
for i, komputer in enumerate(rakit):
    print(f"Komputer {i+1}:")
    # Mengambil data masing-masing komponen dari list
    for komponen in komputer:
        print(f"{komponen.jenis} {komponen.nama} produksi {komponen.merk}")
    print()    
