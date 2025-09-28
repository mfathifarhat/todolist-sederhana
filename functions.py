# Fungsi untuk menampilkan daftar tugas
'''
String diloop dan dimasukkan satu per satu karakter ke dalam variabel judul.
Tiap tugas diberi batas dengan tanda ';' sehingga saat loop mencapai
tanda ';', maka kondisi variabel judul sudah berisi satu judul tugas.
Setelah mencapai tanda ';', print judul dan kosongkan kembali
variabel judul untuk menampung judul tugas lain.

Menggunakan variabel count, menambahkan nilai 1 pada saat 
variabel judul sudah menampung satu judul tugas yang berfungsi
untuk penomoran pada saat menampilkan daftar tugas.
'''
def tampilTugas(tugas):
    judul = ""
    count = 0

    for i in tugas:
        if i == ";":
            if (len(judul) > 1):
                count += 1
                print(f"{count}. {judul}")
            judul = ""
        else:
            judul += i

# Fungsi untuk menambahkan tugas baru
'''
Menggunakan pemisah tanda ';' antar tugas agar dapat mengambil
judul tugas seperti pada fungsi 'tampilTugas()'
'''
def tugasBaru():
    print("Silahkan masukkan tugas baru anda:")
    print("Gunakan tanda ';' untuk memisahkan antar tugas jika ingin menambahkan lebih dari 1")
    print("Contoh : Belajar;Cuci Piring;Masak")
    tugasBaru = input("")
    
    return f"{tugasBaru};" 

# Fungsi untuk mencari tugas berdasarkan kata kunci
'''
Memiliki cara yang sama untuk mengambil tiap judul dengan fungsi 'tampilTugas()'.
Setiap mendapatkan judul tugas, judul tugas akan dicek apakah kata kunci terdapat pada
judul tersebut? Jika iya maka akan masuk ke variabel 'hasil'. Fungsi ini memungkinkan
untuk terdapat dua atau lebih judul tugas yang dikembalikan apabila terdapat dua atau lebih
tugas yang mengandung kata kunci yang diberikan pengguna.
'''
def searchTugas(tugasKu):
    judul = ""
    keyword = input("Silahkan masukkan kata kunci tugas anda!\n")
    hasil = ""
    
    for i in tugasKu:
        if i == ";":
            if (len(judul) > 1 and keyword.upper() in judul.upper()):
                hasil += f"{judul};"
            judul = ""
        else:
            judul += i
            
    return hasil

# Fungsi untuk menandakan suatu tugas sudah selesai
'''
Memiliki cara yang sama untuk mengambil tiap judul dan count untuk perhitungan
dengan fungsi 'tampilTugas()'. Apabila nomor tugas yang dipilih sesuai, maka
judul tugas akan dikembalikan dengan tambahan '(Sudah selesai)' di bagian kanan.
Daftar tugas akan ditampilkan terlebih dahulu sebelum meminta pengguna memasukkan
nomor tugas.
'''
def markDone(tugasKu):
    tampilTugas(tugasKu)
    judul = ""
    nomorKursus = input("Silahkan masukkan nomor tugas yang sudah selesai!\n")
    hasil = ""
    count = 0
    
    for i in tugasKu:
        if i == ";":
            count += 1
            if (str(count) == nomorKursus and len(judul) > 1):
                hasil += f"{judul} (Sudah selesai);"
            else:
                hasil += f"{judul};"
            judul = ""
        else:
            judul += i
            
    return hasil

# Fungsi untuk menandakan suatu tugas sudah selesai
'''
Memiliki cara yang kurang lebih sama dengan fungsi 'markDone', namun perbedaannya
di fungsi ini adalah tugas dengan nomor yang sama dengan input dari pengguna
tidak akan ditambahkan ke variabel hasil sehingga fungsi ini akan mengembalikan
semua tugas kecuali tugas dengan nomor yang sama dengan input dari pengguna.
Daftar tugas akan ditampilkan terlebih dahulu sebelum meminta pengguna memasukkan
nomor tugas.    
'''
def hapusTugas(tugasKu):
    tampilTugas(tugasKu)
    judul = ""
    nomorKursus = input("Silahkan masukkan nomor tugas yang sudah selesai!\n")
    hasil = ""
    count = 0
    
    for i in tugasKu:
        if i == ";":
            count += 1
            if (count != int(nomorKursus) and len(judul) > 1):
                hasil += f"{judul};"
                
            judul = ""
        else:
            judul += i
            
    return hasil

# Fungsi untuk menampilkan daftar tugas
'''
Menggunakan variabel 'totalTugas' dan 'totalSelesai', menambahkan nilai 1 
pada variabel 'totalTugas saat variabel judul sudah menampung satu judul 
tugas yang berfungsi untuk menghitung jumlah tugas dan menambahkan nilai 1 
pada variabel 'totalSelesai' ketika terdapat kata "Sudah selesai" pada 
judul tugas.
Menampilkan statistik dengan mencetak variabel totalTugas untuk Total tugas, 
totalSelesai untuk Total tugas selesai, dan hasil pengurangan dari totalTugas
dengan totalSelesai untuk Total tugas belum selesai.
'''
def tampilStat(tugasKu):
    totalTugas = 0
    totalSelesai = 0
    judul = ""
    
    for i in tugasKu:
        if i == ";":
            if(len(judul) > 1):
                totalTugas += 1
                if ("Sudah selesai" in judul):
                    totalSelesai += 1
            judul = ""
        else:
            judul += i
            
    print("Statistik tugas anda :")
    print(f"Total tugas                 : {totalTugas}")
    print(f"Total tugas selesai         : {totalSelesai}")
    print(f"Total tugas belum selesai   : {totalTugas - totalSelesai}")
    
