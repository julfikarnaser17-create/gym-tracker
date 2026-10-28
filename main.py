import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_latihan.csv")
print(df.head())
print(df.describe())

squat = df[df["latihan"] == "squat"]
bench = df[df["latihan"] == "bench"]


print("Beban bench tertinggi:", bench["beban_kg"].max())
print("Beban squat tertinggi:", squat["beban_kg"].max())

ringkasan = df.groupby("latihan")["beban_kg"].agg(["mean","max","count"])
print(ringkasan)

df["volume"] = df["beban_kg"] * df["repetisi"] * df["set"]
print(df)

df["tanggal"] = pd.to_datetime(df["tanggal"])
for nama, data in df.groupby("latihan"):
  plt.plot(data["tanggal"], data["beban_kg"], marker="o", label=nama)

plt.title("Progres Beban")
plt.xlabel("Tanggal")
plt.ylabel("Beban (kg)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure()

for nama, data in df.groupby("latihan"):
  plt.plot(data["tanggal"], data["volume"], marker="o", label=nama)

plt.title("Progres Volume")
plt.xlabel("Tanggal")
plt.ylabel("Volume (beban x repetisi x set)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


df = df.sort_values(["latihan", "tanggal"])
df["selisih_beban"] = df.groupby("latihan")["beban_kg"].diff()
print(df[["tanggal", "latihan", "beban_kg", "selisih_beban"]])

def cek_stagnan(df, batas=3):
  for nama, data in df.groupby("latihan"):
    terakhir = data["selisih_beban"].tail(batas)
    if (terakhir <= 0).all():
      print(f"{nama}: STAGNAN, coba naikan beban atau ubah program")
    else:
      print(f"{nama}:masih naik, lanjutkan")

cek_stagnan(df)

df["selisih_volume"] = df.groupby("latihan")["volume"].diff()
print(df[["tanggal","latihan","volume","selisih_volume"]])


  


