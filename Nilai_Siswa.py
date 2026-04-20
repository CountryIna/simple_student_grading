print("=== PROGRAM NILAI SISWA ===")
print("\033[0;35;40m Tekan 0 untuk keluar \033[0m")

total = 0
lulus = 0
tidak_lulus = 0

data_nilai = []

while True:
    try:
        nilai = float(input("Masukkan Nilai : "))
    except:
        print("Input harus angka!")
        continue

    if nilai == 0:
        print("Selesai")
        break
    elif nilai <0 or nilai >100:
        print("Input tidak valid.")
    else:
        total +=1
        data_nilai.append(nilai)

        if nilai >= 75:
            print("LULUS")
            lulus +=1
        else:
            print("TIDAK LULUS")
            tidak_lulus +=1

print("\n === HASIL ===")
print("Total Siswa : ", total)
print("Lulus : ", lulus)
print("Tidak Lulus : ", tidak_lulus)
print("Daftar Nilai : ", data_nilai)
print("Nilai Tertinggi : ",max(data_nilai))
print("Nilai Terendah : ",min(data_nilai))
print("Rata-Rata : ", sum(data_nilai) / len(data_nilai))