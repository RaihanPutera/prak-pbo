# Nomor 1
ukuran = int(input("Masukkan ukuran kotak: "))

for i in range(ukuran):
    for j in range(ukuran):
        print("*", end=(""))
    print()    
print()

# Penambahan tipe data / type-hint untuk mempermudah

# Nomor 2
username = str("informatika")
password = str("12345678")

for i in range(4):
    user = str(input("Username anda: "))
    sandi = str(input("Password anda: "))
    
    if (user == username) and (sandi == password):
        print("Berhasil login!")
        break
    else:
        if(i < 3):
            print("Username atau password salah, coba lagi!")
        else:
            print("Maaf, akun anda telah diblokir!")
    print()          