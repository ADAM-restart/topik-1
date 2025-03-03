class Sekolah:
    def __init__(self, nama, alamat, jumlah_siswa):
        # Atribut
        self.nama = nama
        self.alamat = alamat
        self.jumlah_siswa = jumlah_siswa
    
    def tambah_siswa(self, jumlah):
        """Menambah jumlah siswa"""
        self.jumlah_siswa += jumlah
        print(f"Jumlah siswa di {self.nama} bertambah menjadi {self.jumlah_siswa}.")
    
    def kurangi_siswa(self, jumlah):
        """Mengurangi jumlah siswa"""
        if self.jumlah_siswa >= jumlah:
            self.jumlah_siswa -= jumlah
            print(f"Jumlah siswa di {self.nama} berkurang menjadi {self.jumlah_siswa}.")
        else:
            print(f"Jumlah siswa yang dikurangi melebihi jumlah yang ada di {self.nama}.")
    
    def tampilkan_info(self):
        """Menampilkan informasi sekolah"""
        print(f"Nama Sekolah: {self.nama}")
        print(f"Alamat Sekolah: {self.alamat}")
        print(f"Jumlah Siswa: {self.jumlah_siswa}")
        print("-" * 30)

# Membuat objek-objek dari kelas Sekolah
sekolah_abc = Sekolah("Sekolah ABC", "Jl. Pendidikan No. 10", 500)
sekolah_xyz = Sekolah("Sekolah XYZ", "Jl. Ilmu No. 20", 300)
sekolah_mn = Sekolah("Sekolah MN", "Jl. Kreativitas No. 5", 400)

# Menampilkan informasi tentang masing-masing sekolah
sekolah_abc.tampilkan_info()
sekolah_xyz.tampilkan_info()
sekolah_mn.tampilkan_info()

# Menambah siswa di sekolah_abc
sekolah_abc.tambah_siswa(30)

# Mengurangi siswa di sekolah_xyz
sekolah_xyz.kurangi_siswa(50)

# Menampilkan informasi setelah perubahan
sekolah_abc.tampilkan_info()
sekolah_xyz.tampilkan_info()