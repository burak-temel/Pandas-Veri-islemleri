# gerekli kütüphaneler
import pandas as pd
import numpy as np
# veri okuma işlemi
df = pd.read_csv("datasets/nba.csv")
# gösterilecek max satır
pd.set_option('display.max_rows', 10)

# verilerin genel incelenmesi
df.info()

# sütun ve satır sayısının elde edilmesi
df.columns.size
df.index.size
# ilk 5 verinin alınması ".tail() son 5 veri"
df.head()

# Takıma göre gruplayıp takımların oyuncularına ödediği ortalama, max, min ve kaç oyuncu olduğu bilgisine ulaşacağız
df_new = df.groupby("Team")["Salary"].agg([np.mean, np.max, np.min, np.sum])
# sayiya göre saydırıp oyuncu sayısını yeni bir sütun olarak ekliyoruz
df_new["PlayerNumber"] = df.groupby("Team")["Name"].count()

# Takımların belirli poziyonlardaki oyuncu sayısı
df.groupby(["Team", "Position"])["Name"].count()

# Takıma göre pozisyonlardaki ortalama maaş,max ve min
df.groupby(["Team", "Position"])["Salary"].agg([np.mean, np.max, np.min])

# Maaş verilerinde yer alan NaN değerleri ortalama değerler ile değiştirme ve Birden fazla değeri NaN olanları silme
df.dropna(subset=["Name"], how="any", inplace=True)
df_swNaN = df.dropna(subset=["Salary"], how="any", inplace=False)

# Nan değerlerini atmadan da aynı değeri vercektir sadece atma işlemine örnek olsun diye yapıldı
mean = df_swNaN["Salary"].mean()
df__a = df["Salary"].fillna(value=mean, inplace=True)

# filtre işlemleri:
# İsminde John ismi bulunan oyuncuları bulma
# Name string ifadesini ad-Soyad olarak ayırma işlemi
df[["FirstName", "LastName"]] = df["Name"].loc[df["Name"].str.split().str.len()
                                               == 2].str.split(expand=True)
# Sütün sıralaması
df = df[["Name", "FirstName", "LastName", "Team", "Position",
         "Age", "Height", "Weight", "College", "Salary"]]

# Name sütununa ihtiyacımız kalmadığından
df.drop(axis=1, labels="Name", inplace=True)
# FirstName sütununa göre John işlemini arama
df.query("FirstName== 'John'")

#25 yaşından büyüklerin yaşa göre kazanç ortalamaları
df[df["Age"]>=25].groupby("Age")["Salary"].mean()

#isminin içinde Je geçenler
#Kaç tane bozuk- kayıp veri olduğunun kontrolü
df["FirstName"].isna().sum()
df.dropna(subset=["FirstName"],how="all",inplace=True)
df[df["FirstName"].str.find("Je")!=-1]["FirstName"]

#işlenen verinin csv olarak kaydedilmesi
df.to_csv("Nba_yeni.csv")