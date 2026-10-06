import datetime
import random
import getpass

data_barang = {
    "B001": {"nama": "Dompet hitam", "Lokasi": "Kantin", "status": "Belum ditemukan"},
    "B002": {"nama": "Kunci motor", "Lokasi": "Parkiran", "status": "Belum ditemukan"}
}

akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

def login():
    print("\n===== LOGIN =====")
    while True:
        username = input("Username: ")
        try:
            password = getpass.getpass("Password: ")
        except Exception:
            password = input("Password: ")
        if username in akun and akun[username]["password"] == password:
            print("Login berhasil.")
            print("Role:", akun[username]["role"])
            return akun[username]["role"]
        print("Username atau password salah. Silakan coba lagi.")

def tampilkan_data():
    print("\n===== DATA BARANG HILANG =====")
    if len(data_barang) == 0:
        print("Belum ada data barang.")
    else:
        for id_barang, data in data_barang.items():
            print("ID:", id_barang, "| Nama:", data["nama"], "| Lokasi:", data["Lokasi"], "| Status:", data["status"])

def tambah_data():
    print("\n===== TAMBAH DATA =====")
    while True:
        id_barang = input("ID Barang: ").strip()
        if id_barang == "":
            print("ID tidak boleh kosong.")
        elif id_barang in data_barang:
            print("ID sudah digunakan.")
        else:
            break
    while True:
        nama = input("Nama Barang: ").strip()
        if nama == "":
            print("Nama barang tidak boleh kosong.")
        else:
            break
    while True:
        lokasi = input("Lokasi ditemukan/hilang: ").strip()
        if lokasi == "":
            print("Lokasi tidak boleh kosong. ")
        else:
            break
    data_barang[id_barang] = {"nama": nama, "lokasi": lokasi, "status": "Belum ditemukan"}
    waktu = datetime.datetime.now()
    nomor = random.randint(100, 999)
    print("Data barang berhasil ditambahkan. ")
    print("Nomor Laporan:", nomor)
    print("Waktu:", waktu.strftime("%d-%m-%Y %H:%M"))

def ubah_data():
    print("\n===== UBAH DATA =====")
    id_barang = input("Masukkan ID Barang: ").strip()
    if id_barang in data_barang:
        print("1. Ubah Nama ")
        print("2. Ubah Lokasi ")
        print("3. Ubah Status ")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            nama_baru = input("Nama baru: ").strip()
            if nama_baru == "": print("Nama tidak boleh kosong. ")
            else:
                data_barang[id_barang]["nama"] = nama_baru
                print("Nama berhasil diubah. ")
        elif pilihan == "2":
            lokasi_baru = input("Lokasi baru: ").strip()
            if lokasi_baru == "": print("Lokasi tidak boleh kosong. ")
            else:
                data_barang[id_barang]["lokasi"] = lokasi_baru
                print("Lokasi berhasil diubah. ")
        elif pilihan == "3":
            print("1. Belum ditemukan ")
            print("2. Sudah ditemukan ")
            status = input("Pilih status: ")
            if status == "1": data_barang[id_barang]["status"] = "Belum ditemukan"
            elif status == "2": data_barang[id_barang]["status"] = "Sudah ditemukan"
            else:
                print("Pilihan status tidak valid. ")
                return
            print("Status berhasil diubah. ")
        else: print("Pilihan tidak valid. ")
    else: print("ID barang tidak ditemukan. ")

def hapus_data():
    print("\n===== HAPUS DATA =====")
    id_barang = input("Masukkan ID Barang: ").strip()
    if id_barang in data_barang:
        konfirmasi = input("Apakah Anda yakin ingin menghapus data barang ini? (ya/tidak): ").lower()
        if konfirmasi == "ya":
            del data_barang[id_barang]
            print("Data barang berhasil dihapus. ")
        elif konfirmasi == "tidak": print("Penghapusan data dibatalkan. ")
        else: print("Pilihan tidak valid. ")
    else: print("ID barang tidak ditemukan. ")

def menu_admin():
    while True:
        print("\n===== MENU ADMIN =====")
        print("1. Tampilkan Data\n2. Tambah Data\n3. Ubah Data\n4. Hapus Data\n5. Logout ")
        pilihan = input("Pilih: ")
        if pilihan == "1": tampilkan_data()
        elif pilihan == "2": tambah_data()
        elif pilihan == "3": ubah_data()
        elif pilihan == "4": hapus_data()
        elif pilihan == "5": print("Logout berhasil. "); break
        else: print("Pilihan tidak valid. ")

def menu_user():
    while True:
        print("\n===== MENU USER =====")
        print("1. Lihat Data Barang\n2. Logout ")
        pilihan = input("Pilih menu: ")
        if pilihan == "1": tampilkan_data()
        elif pilihan == "2": print("Logout berhasil. "); break
        else: print("Pilihan tidak valid, Menu tidak tersedia. ")

while True:
    print("\n==================================")
    print(" SISTEM PENDATAAN BARANG HILANG ")
    print("====================================")
    try:
        role = login()
        if role == "admin": menu_admin()
        elif role == "user": menu_user()
    except KeyboardInterrupt:
        print("\nProgram dihentikan. ")
        break
    except Exception as error:
        print("Terjadi kesalahan:", error)
        print("Program kembali ke login. ")