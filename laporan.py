print("============SELAMAT DATANG DI PELAPORAN MASYARAKAT============")
print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
#percabangan kehilangan dan fasilitas umum


nik=input("Masukan NIk Anda : ")
nama=input("Masukkan Nama Anda : ")
# tanggal=input("Tanggal : ")
import datetime
tanggal = datetime.datetime.now()
alamat=input("Alamat : ")
notlp=input("Nomer Telepon : ")
jenis=input("Pilih Jenis Laporan [Kehilangan/Fasilitas Umum(FU)] :")
if jenis=="Kehilangan" or jenis=="kehilangan":   
    jenis_laporan="Kehilangan"
elif jenis=="Fasilitas Umum"or jenis=="fasilitas umum" or jenis=="fu" or jenis=="FU":
    jenis_laporan="Fasilitas Umum"
else:
    print("Tidak ada yang di pilih")
    
isilaporan=input("Isi Laporan : ")

print("====================================================================")
print("NIK yang Anda Masukkan adalah : "+nik)
print("Nama yang Anda Masukkan adalah : "+nama)
print("Tanggal Laporan :" , tanggal)
# print("Tanggal yang Anda Masukkan adalah : "+tanggal)
print("Alamat yang Anda Masukkan adalah : "+alamat)
print("Nomer Telepon yang Anda Masukkan adalah : "+notlp)
print("Jenis Laporan yang Anda Masukkan adalah : ",jenis_laporan)
print("Isi Laporan yang Anda Masukkan adalah : "+isilaporan)
print("====================================================================")

check=input("""Tulis "Benar" jika input benar Tulis "Salah" Jika sebaliknya :""")
if check == "Benar" or check =="benar":
    print("Selesai")
elif check == "Salah" or check == "salah":
    print()
else:
    print("Coba Input Ulang")
