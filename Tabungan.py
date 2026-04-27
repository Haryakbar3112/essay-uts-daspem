target = int(input("Masukkan target tabungan: "))

total = 0
hari = 0

while total < target:
    tabungan = int(input("Masukkan tabungan hari ini: "))
    
    total += tabungan
    hari += 1

    print("Total tabungan sementara:", total)

    sisa = target - total
    if sisa > 0:
        print("Sisa yang harus dikumpulkan:", sisa)
    else:
        print("Target sudah tercapai atau terlampaui!")

print("\n=== HASIL ===")
print("Total hari yang dibutuhkan:", hari)