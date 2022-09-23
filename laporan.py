print("============SELAMAT DATANG DI PELAPORAN MASYARAKAT============")
print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
#percabangan kehilangan dan fasilitas umum


nik=input("Masukan NIk Anda : ")
nama=input("Masukkan Nama Anda : ")
# tanggal=input("Tanggal : ")
import datetime
tanggal = datetime.datetime.now()
alamat=input("Alamat : ")
laporan=input("Laporan : ")
#anjing lu semua 



print ("====================================================================")
print ("NIK yang Anda Masukkan adalah : "+nik)
print ("Nama yang Anda Masukkan adalah : "+nama)
print("Tanggal Laporan :" , tanggal)
# print ("Tanggal yang Anda Masukkan adalah : "+tanggal)
print ("Alamat yang Anda Masukkan adalah : "+alamat)
print ("Laporan yang Anda Masukkan adalah : "+laporan)
print ("====================================================================")

check=input("""Tulis "Benar" jika input benar Tulis "Salah" Jika sebaliknya :""")
if check == "Benar" or check =="benar":
    print("Selesai")
elif check == "Salah" or check == "salah":
    print()
else:
    print("Coba Input Ulang")
