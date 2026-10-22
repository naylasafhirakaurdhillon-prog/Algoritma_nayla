#input
tugas = int(input("nilai tugas : "))
uts = int(input("nilai uts : "))
uas = int(input("niai uas : "))
kehadiran = int(input("kehadiran : "))

#hitung nilai akhir
nilai_akhir = ((20% x tugas) + (30% x uts) + (50% x uas), 4)

# syarat kelulusan
lulus = nilai_akhir >= 75 and kehadiran >= 80

# syarat predikat
predikat = (#
    nilai_akhir >= 85
    and kehadiran >= 90
    and nilai_akhir % 2 == 0
)

# output
print(f"nilai akhir : (nilai_akhir)")

if predikat:
    print("status    : LULUS DENGAN PREDIKAT")
elif lulus:
    print("status    : LULUS")
else:
    print("status     : BELUM LULUS")     