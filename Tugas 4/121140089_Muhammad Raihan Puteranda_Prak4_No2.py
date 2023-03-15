# Untuk bisa membuat nilai tangan lawan menjadi random
import random

# Parent class
class Robot:
    jumlah_turn = 0

    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage
    
    def lakukan_aksi(self, a, b, robot_lain):
        Robot.jumlah_turn += 1
        # Jika menang, maka yang akan menyerang adalah robot sendiri, dan jika kalah robot lawan
        if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
            print("Robotmu kalah!")
            robot_lain.aksi(self)
        elif (a == 1 and b == 3) or (a == 3 and b == 2) or (a == 2 and b == 1):
            print("Robotmu menang!")
            self.aksi(robot_lain)
        else:
            print("Hasil seri")    

    # Fungsi akan di override (masing-masing robot punya aksi berbeda)
    def aksi(self):
        pass

# Child class
class Antares(Robot):
    def __init__(self):
        # Inisiasi nama, health, damage, serta atribut tambahan
        super().__init__("Antares", 50000, 5000)
        self.menang = 0
        self.syarat_boost = 3
        self.dmg_boost = 1

    # Overriding fungsi parent class
    def aksi(self, robot_lain):
        self.menang += 1
        # JIka pada turn kelipatan 3 menang, maka serangan akan ditingkatkan
        if (Robot.jumlah_turn % self.syarat_boost == 0):
            robot_lain.health -= self.boost_atk()
            print(f"Antares menyerang sebanyak {self.boost_atk()} DMG")
        else:
            robot_lain.health -= self.damage
            print(f"Antares menyerang sebanyak {self.damage} DMG")

    # Fungsi meningkatkan damage
    def boost_atk(self):
        self.dmg_boost = 1.5
        return self.damage * self.dmg_boost
    
    # Fungsi akan dioverload (masing-masing robot punya informasi yang berbeda)
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"HP: {self.health}")
        print(f"DMG: {self.damage}")
        print("Boost damage: 1.5x pada turn kelipatan 3 jika menang\n")
    
class Alphasetia(Robot):
    def __init__(self):
        # Inisiasi nama, health, damage, serta atribut tambahan
        super().__init__("Alphasetia", 40000, 6000)
        self.menang = 0
        self.syarat_boost = 2
        self.health_boost = 4000
    
    # Overriding fungsi parent class
    def aksi(self, robot_lain):
        self.menang += 1
        # Jika pada turn kelipatan 2 menang, maka health akan ditambah sekaligus menyerang lawan
        if (Robot.jumlah_turn % self.syarat_boost == 0):
            self.health += self.health_boost
            robot_lain.health -= self.damage
            print(f"Alphasetia menambah darah sebanyak {self.health_boost} HP")
            print(f"Alphasetia menyerang sebanyak {self.damage} DMG")
        else:
            robot_lain.health -= self.damage
            print(f"Alphasetia menyerang sebanyak {self.damage} DMG")

    # Fungsi akan dioverload (masing-masing robot punya informasi yang berbeda)
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"HP: {self.health}")
        print(f"DMG: {self.damage}")
        print("Boost health: 4000 pada turn kelipatan 2 jika menang\n")        

class Lecalicus(Robot):
    def __init__(self):
        # Inisiasi nama, health, damage, serta atribut tambahan
        super().__init__("Lecalicus", 45000, 5500)
        self.menang = 0
        self.syarat_boost = 4
        self.health_boost = 7000
        self.dmg_boost = 1

    # Overriding fungsi parent class
    def aksi(self, robot_lain):
        self.menang += 1
        # Jika pada turn kelipatan 4 menang, maka health ditambah dan damage ditingkatkan
        if (Robot.jumlah_turn % self.syarat_boost == 0):
            self.health += self.health_boost
            robot_lain.health -= self.boost_atk()
            print(f"Lecalicus menambah darah sebanyak {self.health_boost} HP")
            print(f"Lecalicus menyerang sebanyak {self.boost_atk()} DMG")
        else:
            robot_lain.health -= self.damage
            print(f"Lecalicus menyerang sebanyak {self.damage} DMG")
    
    # Fungsi meningkatkan damage
    def boost_atk(self):
        self.dmg_boost = 2
        return self.damage * self.dmg_boost
    
    # Fungsi akan dioverload (masing-masing robot punya informasi yang berbeda)
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"HP: {self.health}")
        print(f"DMG: {self.damage}")
        print("Boost damage: 2x dan Boost health: 7000 pada turn kelipatan 4 jika menang\n")

# Overload fungsi info di masing-masing robot
def info_robot(*robots):
    for robot in robots:
        robot.info()

# main

print("Selamat datang di pertandingan robot Yamako")

# List robot
pilihan_robot = [Antares(), Alphasetia(), Lecalicus()]

# Menampilkan informasi robot
print("INFORMASI ROBOT:\n")
info_robot(*pilihan_robot)

# Memilih robot dengan pilihan dikurang 1 untuk cocokkan dengan index di list
robotmu = pilihan_robot[int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")) - 1]
robot_lawan = pilihan_robot[int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): ")) - 1]

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")

turn = 1
# Akan terus bertarung sampai salah satu darah robot habis
while robotmu.health >= 0 and robot_lawan.health >= 0:
    print(f"\nTurn saat ini: {turn}")
    print(f"Robotmu ({robotmu.nama} - {robotmu.health} HP), robot lawan ({robot_lawan.nama} - {robot_lawan.health} HP)")
    
    robotmu_tangan = int(input(f"Pilih tangan robotmu ({robotmu.nama}): "))
    while robotmu_tangan != 1 and robotmu_tangan != 2 and robotmu_tangan != 3:
        print("Input tidak valid!")
        robotmu_tangan = int(input(f"Pilih tangan robotmu ({robotmu.nama}): "))

    # Tangan lawan akan selalu random
    robot_lawan_tangan = random.randint(1, 3)                                
    print(f"Tangan robot lawan ({robot_lawan.nama}): {robot_lawan_tangan}")   

    # Mengakses fungsi parent class untuk menentukan siapa yang menyerang
    robotmu.lakukan_aksi(robotmu_tangan, robot_lawan_tangan, robot_lawan)
    turn += 1

# Ketentuan menang/kalah
if (robotmu.health <= 0):
    print(f"\nRobotmu ({robotmu.nama}) kalah!")
    print(f"Jumlah kemenangan lawan: {robot_lawan.menang}")
elif (robot_lawan.health <= 0):
    print(f"\nSelamat, Robot lawanmu ({robot_lawan.nama}) kalah!")
    print(f"Jumlah kemenanganmu: {robotmu.menang}")
