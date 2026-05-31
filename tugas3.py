# Deklarasi Array (List)
array_gaji = [5000000, 6500000, 9500000]
array_lembur = [30, 32, 34, 36, 38]

print("=== Program Hitung Gaji Karyawan ===")

# Input dari pengguna
golongan = input("Masukkan Golongan (A/B/C) : ").upper()
jam_lembur = int(input("Masukkan Jam Lembur       : "))

gaji_pokok = 0
persen_lembur = 0

# 1. Logika IF untuk menentukan Gaji Pokok dari Array
if golongan == "A":
    gaji_pokok = array_gaji[0]
elif golongan == "B":
    gaji_pokok = array_gaji[1]
elif golongan == "C":
    gaji_pokok = array_gaji[2]
else:
    print("Error: Golongan tidak valid!")
    exit()

# 2. Logika IF untuk menentukan Persentase Lembur dari Array
if jam_lembur == 1:
    persen_lembur = array_lembur[0]
elif jam_lembur == 2:
    persen_lembur = array_lembur[1]
elif jam_lembur == 3:
    persen_lembur = array_lembur[2]
elif jam_lembur == 4:
    persen_lembur = array_lembur[3]
elif jam_lembur >= 5:
    persen_lembur = array_lembur[4]
else:
    persen_lembur = 0 # Jika tidak lembur atau input negatif

# 3. Menggunakan Operator untuk menghitung total
gaji_lembur = gaji_pokok * (persen_lembur / 100)
total_gaji = gaji_pokok + gaji_lembur

# Menampilkan Hasil
print("\n--- Rincian Gaji ---")
print(f"Golongan      : {golongan}")
print(f"Gaji Pokok    : Rp. {int(gaji_pokok):,}")
print(f"Jam Lembur    : {jam_lembur} Jam")
print(f"Gaji Lembur   : Rp. {int(gaji_lembur):,} ({persen_lembur}%)")
print(f"Total Gaji    : Rp. {int(total_gaji):,}")