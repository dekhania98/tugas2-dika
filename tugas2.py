# Program Menghitung Penghasilan Karyawan

print("=== Program Perhitungan Gaji Karyawan ===")

# 1. Mengambil input dari pengguna
golongan = input("Masukkan Golongan Karyawan (A/B/C): ").upper()
jam_lembur = int(input("Masukkan Total Jam Lembur (Angka): "))

# 2. Menentukan Gaji Pokok berdasarkan Golongan menggunakan IF
gaji_pokok = 0
if golongan == 'A':
    gaji_pokok = 5000000
elif golongan == 'B':
    gaji_pokok = 6500000
elif golongan == 'C':
    gaji_pokok = 9500000
else:
    print("Error: Golongan tidak terdaftar. Harap masukkan A, B, atau C.")
    exit() # Menghentikan program jika input salah

# 3. Menentukan persentase gaji lembur berdasarkan jam lembur menggunakan IF
persentase_lembur = 0.0
if jam_lembur == 0:
    persentase_lembur = 0.0
elif jam_lembur == 1:
    persentase_lembur = 0.30
elif jam_lembur == 2:
    persentase_lembur = 0.32
elif jam_lembur == 3:
    persentase_lembur = 0.34
elif jam_lembur == 4:
    persentase_lembur = 0.36
elif jam_lembur >= 5:
    persentase_lembur = 0.38
else:
    print("Error: Jam lembur tidak boleh minus.")
    exit()

# 4. Melakukan perhitungan (menggunakan operator perkalian dan penjumlahan)
gaji_lembur = gaji_pokok * persentase_lembur
total_penghasilan = gaji_pokok + gaji_lembur

# 5. Output / Tampilan ke Layar
print("\n--- Rincian Penghasilan ---")
print(f"Golongan Karyawan : {golongan}")
print(f"Jam Lembur        : {jam_lembur} Jam")
print(f"Gaji Pokok        : Rp {int(gaji_pokok):,}")
print(f"Gaji Lembur       : Rp {int(gaji_lembur):,}")
print("--------------------------- +")
print(f"Jumlah Penghasilan: Rp {int(total_penghasilan):,}")