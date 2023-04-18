from tkinter import *                                       # Mengimport seluruh fungsi tkinter
from tkinter import filedialog, simpledialog, messagebox    # Mengimport fungsi tkinter terpisah untuk bisa diakses
from PIL import ImageTk, Image                              # Mengimport dari modul Python Imaging Library untuk mempermudah edit gambar
import os                                                   # Mengimport fungsi OS

# Membuat jendelan ukuran 1024x600
window = Tk()
window.title("Image Editor (Beta)")
window.geometry("1024x600")

# Membuat menu
menu = Menu(window)
window.config(menu = menu)

# Variabel di set terlebih dahulu agar bisa terdefinisi di seluruh fungsi yang memakainya (global)
path = None
image = None
is_zoomed = False

# Fungsi membuka gambar
def open_image():
    global path, image
    try:
        # Mengambil file bertipe gambar
        path = filedialog.askopenfilename(filetypes = [("Image Files", "*.jpg; *.jpeg; *.png; *bmp")])
        if not (path):
            raise Exception("Tak ada file yang dipilih!")
        else:
            # Mengambil ukuran gambar
            image_size = os.path.getsize(path)
            if (image_size < 10485760):
                
                # Membuka gambar
                image = Image.open(path)
                
                # Ukuran kanvas
                canvas_width = canvas.winfo_width()
                canvas_height = canvas.winfo_height()
                
                # Ukuran gambar & menetapkan aspek rasio (perbandingan lebar & tinggi)
                image_width, image_height = image.size
                aspect_ratio = image_width / image_height
                
                # Menetapkan lebar & tinggi baru agar sesuai dengan kanvas
                new_width = canvas_width
                new_height = int(new_width / aspect_ratio)
                
                if (new_height > canvas_height):
                    new_height = canvas_height
                    new_width = int(new_height * aspect_ratio)
                
                # Menyesuaikan gambar dengan ukuran barunya menggunakan metode interpolasi BICUBIC agar gambar lebih halus
                image = image.resize((new_width, new_height), resample = Image.BICUBIC)

                # Mengubah foto agar bisa ditampilkan ke GUI tkinter
                foto = ImageTk.PhotoImage(image)

                # Menetapkan ukuran baru kanvas
                canvas.config(width = 1024, height = 600)

                # Menghapus gambar yang ada sebelumnya
                canvas.delete("all")

                # Membuat & menampilkan gambar ditengah kanvas, ditentukan oleh titik referensi (anchor) di kiri atas (NW)
                canvas.create_image((canvas.winfo_width() - image.width) // 2, (canvas.winfo_height() - image.height) // 2, anchor = NW, image = foto)
                
                # Menyimpan gambar saat ini
                canvas.image = foto

                # Menyesuaikan gambar pada kanvas saat dilakukan proses minimize / maximize
                configure_image()
            else:
                raise Exception("Maaf, saat ini editor belum mendukung gambar dengan size lebih dari 10 MB")
    except Exception as e:
        messagebox.showerror("Error", str(e))

""" 
Fungsi untuk mengatur gambar agar secara otomatis menyesuaikan kanvas saat program di maximize & minimize
dengan kode yang sama dengan di open_image setelah membuka gambar
"""
def configure_image():
    global image, foto, is_zoomed

    if not (image):
        return

    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    image_width, image_height = image.size
    aspect_ratio = image_width / image_height
    
    new_width = canvas_width
    new_height = int(new_width / aspect_ratio)
    
    if (new_height > canvas_height):
        new_height = canvas_height
        new_width = int(new_height * aspect_ratio)
    
    image = image.resize((new_width, new_height), resample = Image.BICUBIC)
    foto = ImageTk.PhotoImage(image)
    
    canvas.delete("all")
    canvas.create_image((canvas.winfo_width() - image.width) // 2, (canvas.winfo_height() - image.height) // 2, anchor = NW, image = foto)

# Fungsi untuk mengubah ukuran gambar
def resize_image():
    try:
        global image
        if not (image):
            raise Exception("Tak ada gambar yang dipilih!")
        
        # Meminta pengguna memasukkan lebar dan tinggi yang diinginkan dengan nilai minimal yakni 1
        width = simpledialog.askinteger("Resize Image", "Masukkan lebar (dalam piksel):", parent = window, minvalue = 1)
        height = simpledialog.askinteger("Resize Image", "Masukkan tinggi (dalam piksel):", parent = window, minvalue = 1)
        
        # Proses sama seperti saat setelah membuka gambar (menyesuaikan ukuran berdasarkan inputan lebar dan tinggi dari pengguna)
        image = image.resize((width, height), resample = Image.BICUBIC)
        foto = ImageTk.PhotoImage(image)
        
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        image_width, image_height = image.size
        aspect_ratio = image_width / image_height

        new_width = canvas_width
        new_height = int(new_width / aspect_ratio)

        if (new_height > canvas_height):
            new_height = canvas_height
            new_width = int(new_height * aspect_ratio)

        image = image.resize((new_width, new_height), resample = Image.BICUBIC)
        foto = ImageTk.PhotoImage(image)

        canvas.config(width = 1024, height = 600)
        canvas.delete("all")
        canvas.create_image((canvas.winfo_width() - image.width) // 2, (canvas.winfo_height() - image.height) // 2, anchor = NW, image = foto)
        canvas.image = foto
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Fungsi untuk memutar gambar
def rotate_image():
    global image
    if image is not None:
        try:
            # Meminta pengguna untuk input derajat rotasi
            angle = simpledialog.askinteger("Rotate Image", "Masukkan derajat rotasi (0 - 360): ")

            # Saat ini hanya mampu merotasi derajat yang simetris
            if angle in [0, 90, 180, 270, 360]:

                # Merotasi gambar dan mengisi ruang yang kosong
                rotated_image = image.rotate(angle, resample = Image.BICUBIC, expand = True)
                foto = ImageTk.PhotoImage(rotated_image)

                # Menyesuaikan gambar yang telah dirotasi
                canvas.config(width = rotated_image.width, height = rotated_image.height)
                canvas.delete("all")
                canvas.create_image((canvas.winfo_width() - rotated_image.width) // 2, (canvas.winfo_height() - rotated_image.height) // 2, anchor = NW, image = foto)
                
                canvas.image = foto
                image = rotated_image
                configure_image()
            elif (angle is None):
                return
            else:
                raise Exception("Maaf, untuk sekarang gambar hanya bisa dirotate secara simetris!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Tak ada gambar yang dipilih!")

# Fungsi memperbesar gambar
def zoom_in():
    global image, is_zoomed
    if image is not None:
        try:
            # Nilai faktor skala untuk perbesar gambar diset ke 1.25
            scale_factor = 1.25

            # Membuat ukuran baru sesuai gambar yang diperbesar
            new_width = int(image.width * scale_factor)
            new_height = int(image.height * scale_factor)
                
            # Menyesuaikan gambar yang diperbesar    
            zoomed_image = image.resize((new_width, new_height), resample = Image.BICUBIC)
            foto = ImageTk.PhotoImage(zoomed_image)
                
            canvas.delete("all")
            canvas.create_image((canvas.winfo_width() - zoomed_image.width) // 2, (canvas.winfo_height() - zoomed_image.height) // 2,  anchor = NW, image = foto)
                
            canvas.image = foto
            image = zoomed_image

            # Menyatakan gambar sedang diperbesar
            is_zoomed = True
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Tak ada gambar yang dipilih!")

# Fungsi memperkecil gambar
def zoom_out():
    global image, is_zoomed
    if image is not None:
        try:
            # Nilai faktor skala untuk perkecil gambar diset ke 0.8
            scale_factor = 0.8

            # Membuat ukuran baru sesuai gambar yang diperkecil
            new_width = int(image.width * scale_factor)
            new_height = int(image.height * scale_factor)

            # Menyesuaikan gambar yang diperkecil    
            zoomed_image = image.resize((new_width, new_height), resample = Image.BICUBIC)
            foto = ImageTk.PhotoImage(zoomed_image)

            canvas.delete("all")
            canvas.create_image((canvas.winfo_width() - zoomed_image.width) // 2, (canvas.winfo_height() - zoomed_image.height) // 2,  anchor = NW, image = foto)
                
            canvas.image = foto
            image = zoomed_image

            # Menyatakan gambar sedang diperkecil
            is_zoomed = True
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Tak ada gambar yang dipilih!")

# Fungsi mereset gambar menjadi gambar semula
def reset_image():
    global path, image, is_zoomed

    # Menyatakan gambar tidak lagi diperbesar / diperkecil
    is_zoomed = False
    if image is not None:

        # Membuka gambar awal dan akan disesuaikan posisi nya
        image = Image.open(path)
        configure_image()
    else:
        messagebox.showerror("Error", "Tak ada gambar yang dipilih!")

# Fungsi simpan gambar sebagai nama lain
def saveas_image():
    global path, image
    if image is not None:
        
        # Meminta pengguna untuk menentukan tempat dan nama gambar yang ingin disimpan
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                        filetypes = [("PNG Files", "*.png"),
                                                    ("JPEG Files", "*.jpg; *.jpeg"),
                                                    ("Bitmap Files", "*.bmp"),
                                                    ("All Files", "*.*")])
        # Menyimpan gambar
        if (path):
            image.save(path)
    else:
        messagebox.showerror("Error", "Tak ada gambar yang dipilih!")

# Fungsi menyimpan gambar jika ingin alamat dan nama sama, jika tidak maka dilempar ke fungsi save as
def save_image():
    global path, image
    if image is not None:
        if (path):
            image.save(path)
        else:
            saveas_image()
    else:
        messagebox.showerror("Error", "Tak ada gambar yang dipilih!")

# Fungsi penyesuaian gambar yang secara otomatis berjalan jika terjadi suatu kejadian / event
def on_canvas_resize(event):
    global image, foto

    # Jika tidak sedang di perbesar / perkecil, maka sesuaikan gambar seperti biasa
    if not (is_zoomed):
        canvas.delete("all")
        configure_image()

    # Jika sedang di perbesar / perkecil, maka gambar tetap seperti saat di perbesar / perkecil
    else:
        foto = ImageTk.PhotoImage(image)
        canvas.delete("all")
        canvas.create_image((canvas.winfo_width() - image.width) // 2, (canvas.winfo_height() - image.height) // 2, anchor = NW, image = foto)

# Membuat bingkai disebelah kiri untuk menaruh tombol didalamnya 
frame = Frame(window, bg = "blue")
frame.pack(side = LEFT, fill = Y)        

# Membuat pemisah antara kanvas dan bingkai
separator = Frame(window, width = 2, bg = "black")
separator.pack(side = LEFT, fill = Y)

# Membuat kanvas untuk gambar dan menghilangkan border agar terlihat lebih rapih
canvas = Canvas(window, bg = "white", highlightthickness = 0, bd = 0)
canvas.pack(side = RIGHT, fill = BOTH, expand = True)

# Mengikat event Configure / pengubahan ukuran jendela (minimize & maximize) kepada canvas untuk bisa menjalankan fungsi penyesuaian gambar
canvas.bind("<Configure>", on_canvas_resize)

# Membuat menu bernama File yang berisi perintah dasar Open, Save, dan Save as
filemenu = Menu(menu)

# Menon-aktifkan opsi untuk melepaskan sub-menu dari menu sebagai jendela terpisah
filemenu.config(tearoff = False)

# Membuat sub-menu dari menu File
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Open", command = open_image)
filemenu.add_command(label = "Save", command = save_image)
filemenu.add_command(label = "Save as", command = saveas_image)

# Membuat tombol di bingkai untuk mengubah ukuran gambar
resize_image = Button(frame, text = "Resize", command = resize_image)
resize_image.pack(side = TOP, padx = 10, pady = 5)

# Membuat tombol di bingkai untuk memutar gambar
rotate_image = Button(frame, text = "Rotate", command = rotate_image)
rotate_image.pack(side = TOP, padx = 10, pady = 5)

# Membuat tombol di bingkai untuk memperbesar gambar
zoomin_image = Button(frame, text = "Zoom In", command = zoom_in)
zoomin_image.pack(side = TOP, padx = 10, pady = 5)

# Membuat tombol di bingkai untuk memperkecil gambar
zoomout_image = Button(frame, text = "Zoom Out", command = zoom_out)
zoomout_image.pack(side = TOP, padx = 10, pady = 5)

# Membuat tombol di bingkai untuk mengembalikan kondisi awal dari gambar
reset_image = Button(frame, text = "Reset", command = reset_image)
reset_image.pack(side = TOP, padx = 10, pady = 5)

window.mainloop()



