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
jenis=input("Pilih Jenis Laporan [Kehilangan/Fasilitas Umum(FU)] :")
if jenis=="Kehilangan" or jenis=="kehilangan":   
    hilang="Kehilangan"
elif jenis=="Fasilitas Umum" or jenis=="FU":
    fu="Fasilitas Umum"
else:
    print("Tidak ada yang di pilih")

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
