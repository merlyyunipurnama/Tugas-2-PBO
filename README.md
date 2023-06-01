# Tugas 2 Pemrograman Berorientasi Objek

* Nama  : Merly Yuni Purnama
* NPM   : G1A022006
* Kelas : Informatika-B

## Deskripsi Singkat
Kode yang diberikan merupakan implementasi dari tiga kelas yang saling berhubungan, yaitu Mahasiswa, Jurusan, dan Universitas. Kode ini digunakan untuk mengelola informasi tentang mahasiswa, jurusan, dan universitas dalam sebuah sistem.

### Kelas Mahasiswa
Kelas Mahasiswa memiliki atribut-atribut seperti nama, nim, dan jurusan, serta fungsi-fungsi untuk mengakses dan menampilkan informasi mahasiswa. Setiap objek Mahasiswa dapat diinisialisasi dengan atribut-atribut tersebut menggunakan constructor __init__, dan informasi mahasiswa dapat ditampilkan dengan fungsi tampilkanInfo.

### Kelas Jurusan
Kelas Jurusan digunakan untuk merepresentasikan suatu jurusan dalam sebuah universitas. Setiap objek Jurusan memiliki atribut nama jurusan dan daftar mahasiswa yang terdaftar di jurusan tersebut. Objek Mahasiswa dapat ditambahkan ke dalam daftar mahasiswa jurusan menggunakan fungsi tambahMahasiswa. Selain itu, kelas ini juga memiliki fungsi tampilkanDaftarMahasiswa untuk menampilkan daftar mahasiswa dalam jurusan tersebut.

### Kelas Universitas
Kelas Universitas merepresentasikan sebuah universitas yang terdiri dari beberapa jurusan. Setiap objek Universitas memiliki atribut nama universitas dan daftar jurusan yang ada di universitas tersebut. Objek Jurusan dapat ditambahkan ke dalam daftar jurusan universitas menggunakan fungsi tambahJurusan. Kelas ini juga memiliki fungsi tampilkanDaftarJurusan untuk menampilkan daftar jurusan yang ada di universitas.

#### Penggunaan Kode
Untuk menggunakan kode ini, langkah-langkah yang dapat dilakukan antara lain:

1. Membuat objek-objek mahasiswa menggunakan kelas Mahasiswa. Setiap objek mahasiswa diinisialisasi dengan atribut-atribut seperti nama, nim, dan jurusan.

2. Membuat objek-objek jurusan menggunakan kelas Jurusan. Setiap objek jurusan diinisialisasi dengan atribut nama jurusan.

3. Menambahkan objek mahasiswa ke dalam daftar mahasiswa pada objek jurusan menggunakan fungsi tambahMahasiswa.

4. Membuat objek universitas menggunakan kelas Universitas. Setiap objek universitas diinisialisasi dengan atribut nama universitas.

5. Menambahkan objek jurusan ke dalam daftar jurusan pada objek universitas menggunakan fungsi tambahJurusan.

6. Menampilkan informasi mengenai daftar jurusan di universitas menggunakan fungsi tampilkanDaftarJurusan.

7. Menampilkan daftar mahasiswa dalam setiap jurusan menggunakan fungsi tampilkanDaftarMahasiswa pada objek jurusan.

Contoh program sederhana untuk mengelola data mahasiswa di sebuah universitas XYZ :
https://github.com/merlyyunipurnama/Tugas-2-PBO/blob/main/Code-Tugas-2.py
