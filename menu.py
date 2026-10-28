import pandas as pd
import matplotlib.pyplot as plt
from tambah import tambah_latihan

def muat_data():
  df = pd.read_csv("data_latihan.csv")
  df["tanggal"] = pd.to_datetime(df["tanggal"])
  df["volume"] = df["beban_kg"] * df["repetisi"] * df["set"]
  df = df.sort_values(["latihan", "tanggal"])
  df["selisih_beban"] = df.groupby("latihan")["beban_kg"].diff()
  return df

def lihat_riwayat():
  df = muat_data()
  print(df[["tanggal", "latihan", "beban_kg", "repetisi", "set", "volume"]])

def tampil_grafik(kolom, judul):
  df = muat_data()
  for nama, data in df.groupby("latihan"):
   plt.plot(data["tanggal"], data[kolom], marker="o", label=nama)
  plt.title(judul)
  plt.xlabel("Tanggal")
  plt.ylabel(kolom)
  plt.legend()
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

def cek_stagnan(batas=3):
  df = muat_data()
  for nama, data in df.groupby("latihan"):
    terakhir = data["selisih_beban"].tail(batas)
    if (terakhir <= 0).all():
      print(f"{nama}: STAGNAN, coba naikkan beban atau ubah program")
    else:
      print(F"{nama}: masih naik, lanjutkan")

def menu():
  while True:
    print("\n=== GYM TRACKER ===")
    print("1. Tambah latihan")
    print("2. Lihat riwayat")
    print("3. Grafik beban")
    print("4. Grafik volume")
    print("5. Cek stagnan")
    print("0. keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
      tambah_latihan()
    elif pilihan == "2":
      lihat_riwayat()
    elif pilihan == "3":
      tampil_grafik("beban_kg", "Progres Beban")
    elif pilihan == "4":
      tampil_grafik("volume", "Progres Volume")
    elif pilihan == "5":
      cek_stagnan()
    elif pilihan == "0":
      print("Sampai jumpa!")
      break
    else:
      print("Pilihan tidak valid, coba lagi.")

menu()