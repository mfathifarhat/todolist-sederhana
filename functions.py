# Fungsi untuk menampilkan daftar tugas
'''
String diloop dan dimasukkan satu per satu karakter ke dalam variabel judul.
Tiap tugas diberi batas dengan tanda ';' sehingga saat loop mencapai
tanda ';', maka kondisi variabel judul sudah berisi satu judul tugas.
Setelah mencapai tanda ';', print judul dan kosongkan kembali
variabel judul untuk menampung judul tugas lain.
'''
def tampilTugas(tugas):
    judul = ""
    count = 0

    for i in tugas:
        if i == ";":
            count += 1
            if (len(judul) > 1):
                print(f"{count}. {judul}")
            judul = ""
        else:
            judul += i

# Fungsi untuk menambahkan tugas baru
def tugasBaru():
    print("Silahkan masukkan tugas baru anda:")
    print("Gunakan tanda ';' pada tiap tugas jika ingin menambahkan lebih dari 1")
    print("Contoh : Belajar;Cuci Piring;Masak")
    tugasBaru = input("")
    
    return f"{tugasBaru};" 

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
    
