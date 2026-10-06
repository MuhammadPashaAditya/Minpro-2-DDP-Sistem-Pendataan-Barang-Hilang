Nama : Muhammad Pasha Aditya
NIM  : 2609116085
Kelas: C

Berikut deskripsi singkat program saya:

Sistem Pendataan Barang Hilang

Program ini dibuat untuk membantu mencatat data barang yang hilang atau ditemukan. Pengguna harus melakukan login terlebih dahulu sebelum masuk ke menu program.
Program memiliki dua role, yaitu admin dan user. Admin dapat melihat, menambah, mengubah, dan menghapus data barang. Sedangkan user hanya dapat melihat data barang yang sudah tersimpan.
Data barang yang dicatat meliputi ID barang, nama barang, lokasi, dan status barang. Program juga memiliki validasi input supaya kesalahan saat memasukkan data tidak langsung membuat program berhenti.

Berikut ini adalah Flowchart saya:
<img width="3116" height="6228" alt="image" src="https://github.com/user-attachments/assets/b6e7e71f-926b-4077-a092-0c0bb3e8a5b5" />
Sebelum saya menjelaskan alurnya, saya ingin berterimakasih atas Masukan Aslab saya yaitu Bang Dylan karena di MINPRO 1 alur saya berantakan dan symbolnya tidak menempel. Disini telah saya evaluasi.
Berikut penjelasan alur nya:
Program dimulai dari halaman login. Pengguna memasukkan username dan password. Jika data login salah, pengguna akan diminta mencoba kembali.
Jika login berhasil, program mengecek role pengguna.

Admin masuk ke menu admin dan dapat melakukan:
-Melihat data
-Menambah data
-Mengubah data
-Menghapus data
-Logout
-User hanya dapat melihat data barang dan melakukan logout.

Pada saat memasukkan data, program melakukan pengecekan terlebih dahulu. Jika input tidak sesuai, pengguna akan diminta memasukkan data kembali.
Setelah logout, pengguna dapat kembali ke halaman login.

Selanjutnya dokumentasi Program dan Output:
Tampilan Login

Pada bagian awal, pengguna harus memasukkan username dan password yang sudah tersedia.
===== LOGIN =====
Username: admin
Password: admin123
Login berhasil.
Role: admin
Disini juga saya menggunakan Getpass yang dimana saat menginput pass yang bersifat pribadi tanpa menampilkan dilayar
<img width="366" height="207" alt="Screenshot (70)" src="https://github.com/user-attachments/assets/4ae51416-3c3e-404a-a624-2e51697c6947" />
Pada saat memasuki menu Admin:
Setelah login sebagai admin, akan muncul beberapa pilihan menu:

===== MENU ADMIN =====
1. Tampilkan Data
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Logout

Admin memiliki akses lebih banyak karena dapat mengelola data barang.
<img width="539" height="113" alt="menu admin minpro2" src="https://github.com/user-attachments/assets/c06885f7-b7b5-4475-8c2f-89d1a978982c" />

Selanjutnya bagian data:
Menampilkan Data
Contoh data yang ditampilkan:

===== DATA BARANG HILANG =====
ID: B001 | Nama: Dompet hitam | Lokasi: Kantin | Status: Belum ditemukan
ID: B002 | Nama: Kunci motor | Lokasi: Parkiran | Status: Belum ditemukan
<img width="593" height="83" alt="MenuData" src="https://github.com/user-attachments/assets/e154cf6f-f21d-4f7f-9d20-70a66f713874" />

Menambah Data
Admin dapat memasukkan data barang baru melalui menu tambah data.

===== TAMBAH DATA =====
ID Barang: B003
Nama Barang: Botol minum
Lokasi ditemukan/hilang: Ruang kelas
Data berhasil ditambahkan.
<img width="323" height="273" alt="tambah data minpro2" src="https://github.com/user-attachments/assets/12572e4c-b1b0-45a5-8058-b0fa26b4cbac" />


Mengubah Data
Admin dapat memilih ID barang yang ingin diubah, kemudian memilih bagian data yang ingin diperbarui.
<img width="273" height="192" alt="ubahdata minpro2" src="https://github.com/user-attachments/assets/2143cfae-1c74-4ff2-a588-68af41e1c50e" />

Menghapus Data
Admin juga dapat menghapus data berdasarkan ID barang. Sebelum data dihapus, program meminta konfirmasi terlebih dahulu.
<img width="501" height="237" alt="hapusdata minpro2" src="https://github.com/user-attachments/assets/19c2fd73-45b2-4c1c-81a8-71ac4c53d195" />

Selanjutnya saat login menjadi user:
Menu User

Jika login menggunakan role user, menu yang tersedia lebih terbatas:
===== MENU USER =====
1. Lihat Data Barang
2. Logout

User hanya dapat melihat data dan tidak dapat menambah, mengubah, atau menghapus data.
<img width="548" height="271" alt="menu user minpro2" src="https://github.com/user-attachments/assets/57712369-25e1-4c55-9fda-0af353a01d65" />

Pada program ini terdapat beberapa penerapan tambahan, yaitu:

-Login dan role pengguna, sehingga admin dan user memiliki hak akses yang berbeda.
-Validasi input, untuk mencegah data kosong atau input yang tidak sesuai.
-Error handling, sehingga kesalahan input tidak langsung menghentikan program.
-Menggunakan Dictionary untuk menyimpan data barang.
-Menggunakan Function agar bagian program seperti login dan pengolahan data lebih mudah dipisahkan.
