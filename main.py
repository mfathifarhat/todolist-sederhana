from functions import *

tugasKu = ""

def tampilMenu():
    global tugasKu
    
    print(f"""
Menu :
1. Tampilkan daftar tugas
2. Tambah tugas baru
3. Cari tugas
4. Tandai tugas sudah selesai
5. Hapus tugas
6. Tampilkan statistik 
0. Exit     
""")
    
    selectMenu = input("")

    match selectMenu:
        case "1":
            print("Daftar tugas anda:")
            tampilTugas(tugasKu)
            if len(tugasKu.replace(";", "")) < 1:
                print("Yayy lagi ga ada tugas nih! ヾ(≧▽≦*)o")
        case "2":
            tambahTugas = tugasBaru()
            if len(tambahTugas.replace(";", "")) > 0:
                tugasKu += tambahTugas
                print("Tugas berhasil ditambahkan!")
        case "3":
            hasil = searchTugas(tugasKu)
            if len(hasil.replace(";","")) < 1:
                print("Hasil pencarian tidak ditemukan. (；′⌒`)")
            else:
                print("Hasil pencarian :")
                tampilTugas(hasil)
        case "4":
            done = markDone(tugasKu)
            if "Sudah selesai" in done:
                tugasKu = done
                print("Yayy!! Satu tugas sudah selesai! ヾ(≧▽≦*)o")
            else:
                print("Nomer tugas tidak sesuai! o((>ω< ))o")
        case "5":
            hapus = hapusTugas(tugasKu)
            if len(hapus) < len(tugasKu):
                tugasKu = hapus
                print("Tugas berhasil dihapus! ヾ(≧▽≦*)o")
            else:
                print("Nomer tugas tidak sesuai! o((>ω< ))o")
        case "6":
            tampilStat(tugasKu)
        case "0":
            exit()
        case _:
            print("Silahkan pilih nomor menu yang sesuai! o((>ω< ))o")
            
    tampilMenu()

print("Selamat Datang Kembali! o(*￣▽￣*)ブ")

tampilMenu()


        
        
        
