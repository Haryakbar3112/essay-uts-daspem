total_telur = 0
nama_kandang = input("Masukkan nama kandang: ").strip()
for hari in range(1, 8):
    print(f"Hari ke-{hari}")
    jumlah_ayam = int(input("Masukkan jumlah ayam: "))
    jumlah_telur = int(input("Masukkan jumlah telur yang dihasilkan: "))
    if jumlah_ayam > 0:
        rata_rata = jumlah_telur / jumlah_ayam
    else:
        rata_rata = 0
    if rata_rata >= 0.8:
        kategori = "Produktif tinggi"
    elif rata_rata >= 0.5:
        kategori = "Produktif sedang"
    else:
        kategori = "Produktif rendah"
    total_telur += jumlah_telur
    print("Laporan harian:")
    print(f"Kandang       : {nama_kandang}")
    print(f"Jumlah ayam   : {jumlah_ayam}")
    print(f"Jumlah telur  : {jumlah_telur}")
    print(f"Rata-rata     : {rata_rata:.2f} telur per ayam")
    print(f"Kategori      : {kategori}")
    print("-" * 30)

print("Laporan total selama 7 hari:")
print(f"  Total telur   : {total_telur}")