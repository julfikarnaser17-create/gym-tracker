import pandas as pd
from datetime import datetime


GERAKAN_VALID = ["bench","squat"]


def minta_angka(pesan, tipe=float):
  while True:
    try:
      nilai = tipe(input(pesan))
      if nilai <= 0:
        print("Angka harus lebih dari 0.")
        continue
      return nilai
    except ValueError:
      print("Masukan angka yang valid.")


def minta_tanggal(pesan):
  while True:
    teks = input(pesan)
    try:
      datetime.strptime(teks, "%Y-%m-%d")
      return teks
    except ValueError:
      print("Format salah. Contoh: 2026-10-20")

def minta_gerakan():
  while True:
    teks = input(f"Gerakan({'/'.join(GERAKAN_VALID)}): ").lower().strip()
    if teks in GERAKAN_VALID:
      return teks
    print("Gerakan tidak dikenal, coba lagi.")


def tambah_latihan():
  tanggal = minta_tanggal("Tanggal (YYYY-MM-DD): ")
  latihan = minta_gerakan()
  beban = minta_angka("Beban (kg): ", float)
  repetisi = minta_angka("Repetisi: ", int)
  jumlah_set = minta_angka("Jumlah set: ", int)

  baris = pd.DataFrame([{
    "tanggal": tanggal,
    "latihan": latihan,
    "beban_kg": beban,
    "repetisi": repetisi,
    "set": jumlah_set,
  }])
  baris.to_csv("data_latihan.csv", mode="a", header=False, index=False)
  print("Tersimpan!")


