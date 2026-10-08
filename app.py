import time

def tampilkan_menu():
    print("=" * 40)
    print("    APLIKASI MANAJEMEN TUGAS DEVOPS")
    print("=" * 40)
    print("1. Lihat Status Server")
    print("2. Jalankan Deployment")
    print("3. Tampilkan Log Sistem")
    print("4. Keluar")
    print("=" * 40)

def cek_status():
    print("\n[INFO] Memeriksa status server...")
    time.sleep(1)
    print("[OK] Server berjalan dengan lancar (Uptime: 99.9%)\n")

def jalankan_deploy():
    print("\n[PROCESS] Memulai proses deployment...")
    time.sleep(1)
    print("[SUCCESS] Kode berhasil di-deploy ke server staging!\n")

def lihat_log():
    print("\n[LOGS] Menampilkan log aktivitas terakhir:")
    print("- 10:00:00 WIB - Build succeeded")
    print("- 10:05:00 WIB - Container started")
    print("- 10:10:00 WIB - Health check status: OK\n")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            cek_status()
        elif pilihan == '2':
            jalankan_deploy()
        elif pilihan == '3':
            lihat_log()
        elif pilihan == '4':
            print("\nTerima kasih! Keluar dari aplikasi.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
