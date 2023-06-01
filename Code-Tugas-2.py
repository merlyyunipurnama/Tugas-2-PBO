#========================================================= Kelas Mahasiswa =========================================================#

# Membuat Class untuk Mahasiswa
class Mahasiswa:
    
    # Membuat init function atau constructor dari kelas Mahasiswa sehingga ketika objek dibuat, bisa langsung mendefinisikan atributnya
    def __init__(self, nama, nim, jurusan):
        self.nama    = nama
        self.nim     = nim
        self.jurusan = jurusan
    
    # Membuat fungsi untuk menampilkan daftar atribut dari kelas Mahasiswa
    def tampilkanInfo(self):
        print("Nama    :", self.nama)
        print("NIM     :", self.nim)
        print("Jurusan :", self.jurusan)
        
"""Kode diatas merupakan implementasi dari sebuah kelas bernama Mahasiswa
   * def __init__(self, nama, nim, jurusan): Fungsi ini akan dipanggil ketika objek Mahasiswa dibuat 
     dan memiliki empat parameter, yaitu self, nama, nim, dan jurusan.
     
   * def tampilkanInfo(self): Fungsi ini bertujuan untuk menampilkan informasi 
     atau atribut yaitu nama, nim, dan jurusan dari objek Mahasiswa. """

#========================================================= Kelas Jurusan ==========================================================#

# Membuat kelas Jurusan
class Jurusan:
    
    # Membuat init function atau constructor dari kelas Jurusan sehingga ketika objek dibuat, kita bisa langsung mendefinisikan atributnya
    def __init__(self, nama_jurusan):
        self.namaJurusan = nama_jurusan
        self.daftarMahasiswa = []
    
    # Membuat fungsi untuk menambah objek Mahasiswa baru ke dalam atribut daftar_mahasiswa
    def tambahMahasiswa(self, mahasiswa):
        self.daftarMahasiswa.append(mahasiswa)
    
    # Membuat fungsi untuk menampilkan daftar mahasiswa pada jurusan di kelas Jurusan saat ini
    def tampilkanDaftarMahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.namaJurusan)
        for mahasiswa in self.daftarMahasiswa:
            mahasiswa.tampilkanInfo()
            
"""Kode diatas merupakan implementasi dari kelas bernama Jurusan
   * def __init__(self, nama_jurusan): merupakan constructor atau inisialisasi objek kelas 
     yang akan dipanggil ketika objek Jurusan dibuat dan memiliki dua parameter, yaitu self dan nama_jurusan.
     
   * def tambahMahasiswa(self, mahasiswa): Fungsi untuk menambahkan objek Mahasiswa 
     ke dalam atribut daftarMahasiswa pada objek Jurusan dan memiliki dua parameter yaitu self dan mahasiswa.
     
   * def tampilkanDaftarMahasiswa(self): Fungsi untuk menampilkan daftar mahasiswa yang terkait dengan objek Jurusan
     dan memiliki satu parameter yaitu self. """

#======================================================= Kelas Universitas ========================================================#

# Membuat kelas Universitas
class Universitas:
    
    # Membuat init function atau constructor dari kelas Universitas sehingga ketika objek dibuat, kita bisa langsung mendefinisikan atributnya
    def __init__(self, nama_universitas):
        self.namaUniversitas = nama_universitas
        self.daftarJurusan = []
    
    # Membuat fungsi untuk menambah objek Jurusan baru ke dalam atribut daftar_jurusan
    def tambahJurusan(self, jurusan):
        self.daftarJurusan.append(jurusan)
    
    # Membuat fungsi untuk menampilkan daftar jurusan di kelas Universitas saat ini
    def tampilkanDaftarJurusan(self):
        print("Daftar Jurusan di Universitas", self.namaUniversitas)
        for jurusan in self.daftarJurusan:
            print("- Nama Jurusan:", jurusan.namaJurusan)
            
"""Kode diatas merupakan implementasi dari kelas bernama Universitas
   * def __init__(self, nama_universitas): merupakan constructor atau inisialisasi yang akan dipanggil 
     ketika objek Universitas dibuat. Fungsi ini memiliki dua parameter, yaitu self dan nama_universitas.
     
   * def tambahJurusan(self, jurusan): fungsi untuk menambahkan objek Jurusan ke dalam atribut daftarJurusan 
     pada objek Universitas saat ini. Fungsi ini memiliki dua parameter yaitu self dan jurusan.
     
   * def tampilkanDaftarJurusan(self): fungsi untuk menampilkan daftar jurusan yang terkait dengan objek
     Universitas saat ini dan memiliki satu parameter yaitu self, yang juga merupakan referensi ke objek tersebut. """
     
#======================================================= Objek Universitas ========================================================#

# Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

""" Kode diatas berfungsi untuk membuat objek Universitas dengan nama XYZ University """

#================================================== Objek Jurusan & Mahasiswa =====================================================#

# Membuat objek Jurusan "Teknik Informatika" dan daftar mahasiswa
jurusanTi  = Jurusan("Teknik Informatika")
mahasiswa1 = Mahasiswa("Merly Yuni Purnama", "G1A022006", "Teknik Informatika")
jurusanTi.tambahMahasiswa(mahasiswa1)

# Membuat objek Jurusan "Teknik Sipil" dan daftar mahasiswa
jurusanTs  = Jurusan("Teknik Sipil")
mahasiswa2 = Mahasiswa("Mutia Qatrunnada", "G1B022002", "Teknik Sipil")
jurusanTs.tambahMahasiswa(mahasiswa2)

# Membuat objek Jurusan "Teknik Mesin" dan daftar mahasiswa
jurusanTm  = Jurusan("Teknik Mesin")
mahasiswa3 = Mahasiswa("Musdalifah Hasibuan", "G1C022005", "Teknik Mesin")
jurusanTm.tambahMahasiswa(mahasiswa3)

# Membuat objek Jurusan "Teknik Elektro" dan daftar mahasiswa
jurusanTe  = Jurusan("Teknik Elektro")
mahasiswa4 = Mahasiswa("Cadilla Septi Natali", "G1D022007", "Teknik Elektro")
jurusanTe.tambahMahasiswa(mahasiswa4)

# Membuat objek Jurusan "Arsitektur" dan daftar mahasiswa
jurusanArsi = Jurusan("Arsitektur")
mahasiswa5  = Mahasiswa("Amara Putri", "G1E022003", "Arsitektur")
jurusanArsi.tambahMahasiswa(mahasiswa5)

# Membuat objek Jurusan "Sistem Informasi" dan daftar mahasiswa
jurusanSi   = Jurusan("Sistem Informasi")
mahasiswa6  = Mahasiswa("Ulpa", "G1F022002", "Sistem Informasi")
jurusanSi.tambahMahasiswa(mahasiswa6)

# Menambahkan jurusan ke dalam Universitas
universitas_xyz.tambahJurusan(jurusanTi)
universitas_xyz.tambahJurusan(jurusanTs)
universitas_xyz.tambahJurusan(jurusanTm)
universitas_xyz.tambahJurusan(jurusanTe)
universitas_xyz.tambahJurusan(jurusanArsi)
universitas_xyz.tambahJurusan(jurusanSi)

""" * Kode diatas berfungsi untuk membuat objek Jurusan dengan nama Teknik Informatika, Teknik Sipil, 
      Teknik Mesin, Teknik Elektro, Arsitektur, dan Sistem Informasi. 
      Kemudian menambahkan semuanya ke daftar jurusan yang ada di XYZ University
     
    * Kode diatas berfungsi untuk membuat objek Mahasiswa dengan nama-nama mahasiswa yang ada di tiap jurusan 
      dan memasukkannya ke dalam jurusan-jurusan yang ada di XYZ University. """

#========================================= Menampilkan Daftar Jurusan & Mahasiswa =============================================#
     
# Menampilkan daftar jurusan di Universitas
universitas_xyz.tampilkanDaftarJurusan()
print("=======================================================")

# Menampilkan daftar mahasiswa di Jurusan "Teknik Informatika"
jurusanTi.tampilkanDaftarMahasiswa()
print("=======================================================")

# Menampilkan daftar mahasiswa di Jurusan "Teknik Sipil"
jurusanTs.tampilkanDaftarMahasiswa()
print("=======================================================")

# Menampilkan daftar mahasiswa di Jurusan "Teknik Mesin"
jurusanTm.tampilkanDaftarMahasiswa()
print("=======================================================")

# Menampilkan daftar mahasiswa di Jurusan "Teknik Elektro"
jurusanTe.tampilkanDaftarMahasiswa()
print("=======================================================")

# Menampilkan daftar mahasiswa di Jurusan "Arsitektur"
jurusanArsi.tampilkanDaftarMahasiswa()
print("=======================================================")

# Menampilkan daftar mahasiswa di Jurusan "Sistem Informasi"
jurusanSi.tampilkanDaftarMahasiswa()
print("=======================================================")

""" Kode di atas digunakan untuk menampilkan daftar jurusan yang ada 
    di Universitas XYZ dan daftar mahasiswa di setiap jurusan . """
