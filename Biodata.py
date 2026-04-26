# Program untuk menerima input biodata mahasiswa

nama = input("Masukkan nama mahasiswa: ")  # STRING - menerima teks nama
umur = int(input("Masukkan umur mahasiswa: "))  # INTEGER - menerima bilangan bulat
ipk = float(input("Masukkan IPK mahasiswa: "))  # FLOAT - menerima bilangan desimal

print(f"Nama: {nama}")  # Menampilkan STRING
print(f"Umur: {umur}")  # Menampilkan INTEGER
print(f"IPK: {ipk}")  # Menampilkan FLOAT

# Contoh BOOLEAN
print("\n--- Contoh Tipe Data BOOLEAN ---")
adalah_mahasiswa = True  # BOOLEAN - nilai True
sudah_lulus = False      # BOOLEAN - nilai False
print(f"Adalah mahasiswa: {adalah_mahasiswa}")
print(f"Sudah lulus: {sudah_lulus}")