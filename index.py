from matkul.show import lihat
from matkul.create import membuat
from matkul.update import update_record
from matkul.delete import delete_record

def main():
    while True:
        print("\nMODIFIKASI DATABASE")
        print("-----------------------------------------")
        print("1. CREATE")
        print("2. READ")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. EXIT")
        print("-----------------------------------------")

        pil = int(input("MASUKKAN PILIHAN: "))

        if pil == 1:
            id = int(input("Masukkan  id: "))
            agama = input("masukan agama yang kamu anut: ")
            nama = input("Masukkan nama: ")
            membuat( id, agama, nama )
            print("Data berhasil ditambahkan.")
            lihat()
        elif pil == 2:
            lihat()
        elif pil == 3:
            id = int(input("Masukkan ID : "))
            nama = input("Masukkan nama : ")
            agama = input("Masukkan agama yang kamu anut: ")
            update_record(id, nama, agama)
            print("Data berhasil diupdate.")
            lihat()
        elif pil == 4:
            id = int(input("Masukkan ID staf kantor yang mau dihapus: "))
            delete_record(id)
            print("Data berhasil dihapus.")
            lihat()
        elif pil == 5:
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak ada. Silakan coba lagi.")

if __name__ == "__main__":
    main()