##############################################################
# BG-NBD ve Gamma-Gamma ile CLTV Prediction
##############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO satış ve pazarlama faaliyetleri için roadmap belirlemek istemektedir.
# Şirketin orta uzun vadeli plan yapabilmesi için var olan müşterilerin gelecekte şirkete sağlayacakları potansiyel değerin tahmin edilmesi gerekmektedir.


###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi


###############################################################
# GÖREVLER
###############################################################
# GÖREV 1: Veriyi Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.Dataframe’in kopyasını oluşturunuz.
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions
df_=pd.read_csv("DERSLER/CRM/Case Study-FLOMusteriSegmentasyonu/FLOMusteriSegmentasyonu/flo_data_20k.csv")
df=df_.copy()
pd.set_option("display.max_columns", None)
df.head()
           # 2. Aykırı değerleri baskılamak için gerekli olan outlier_thresholds ve replace_with_thresholds fonksiyonlarını tanımlayınız.
def outlier_thresholds(dataframe,variable):
    quartile1 = dataframe[variable].quantile(0.25)
    quartile3 = dataframe[variable].quantile(0.75)
    interquantile_range= quartile3 - quartile1
    up_limit= quartile3 + 1.5 * interquantile_range
    low_limit= quartile1- 1.5* interquantile_range
    return low_limit, up_limit

def replace_with_threshold(dataframe,variable):
    low_limit, up_limit = outlier_thresholds(dataframe,variable)
    dataframe.loc[(dataframe[variable]<low_limit),variable] = low_limit #eger low_limden dusuk deger varsa onu low_limite esitle.
    dataframe.loc[(dataframe[variable]>up_limit),variable] = up_limit #eger up_limden yuksek deger varsa onu up_limite esitle.

           # Not: cltv hesaplanırken frequency değerleri integer olması gerekmektedir.Bu nedenle alt ve üst limitlerini round() ile yuvarlayınız.
           # 3. "order_num_total_ever_online","order_num_total_ever_offline","customer_value_total_ever_offline","customer_value_total_ever_online" değişkenlerinin
           # aykırı değerleri varsa baskılayanız.
df.describe().T
replace_with_threshold(df,"order_num_total_ever_online")
replace_with_threshold(df,"order_num_total_ever_offline")
replace_with_threshold(df,"customer_value_total_ever_offline")
replace_with_threshold(df,"customer_value_total_ever_online")
    df.describe().T
           # 4. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
    df["total_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
    df["total_order"] = df["order_num_total_ever_offline"] + df["order_num_total_ever_online"]
           # 5. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
           df["first_order_date"] = pd.to_datetime(df["first_order_date"])
           df["last_order_date"] = pd.to_datetime(df["last_order_date"])
           df["last_order_date_offline"] = pd.to_datetime(df["last_order_date_offline"])
           df["last_order_date_online"] = pd.to_datetime(df["last_order_date_online"])
           df.dtypes

# GÖREV 2: CLTV Veri Yapısının Oluşturulması
           # 1.Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi olarak alınız.
import datetime as dt
df["last_order_date"].max()  #last date: ('2021-05-30 00:00:00')
today_date = dt.datetime(2021, 6, 1)
df.head()
           # 2.customer_id, recency_cltv_weekly, T_weekly, frequency ve monetary_cltv_avg değerlerinin yer aldığı yeni bir cltv dataframe'i oluşturunuz.
           cltv = pd.DataFrame(columns=["customer_id", "recency_cltv_weekly", "T_weekly", "frequency", "monetary_cltv_avg"])
df.head()
cltv.head()
           # Monetary değeri satın alma başına ortalama değer olarak, recency ve tenure değerleri ise haftalık cinsten ifade edilecek.
cltv["recency_cltv_weekly"] =(df["last_order_date"]- df["first_order_date"]) /7
cltv["T_weekly"] =(today_date - df["first_order_date"])/7
cltv["monetary_cltv_avg"] =df["total_value"] / df["total_order"]
cltv["customer_id"] = df["master_id"]
cltv["frequency"] = df["total_order"]
cltv = cltv[cltv["frequency"]>0.9]
cltv = cltv[cltv["recency_cltv_weekly"] != 0]
cltv.head()
# GÖREV 3: BG/NBD, Gamma-Gamma Modellerinin Kurulması, CLTV'nin hesaplanması
           # 1. BG/NBD(satın alma sayısı) modelini fit ediniz.
                # a. 3 ay içerisinde müşterilerden beklenen satın almaları tahmin ediniz ve exp_sales_3_month olarak cltv dataframe'ine ekleyiniz.
                # b. 6 ay içerisinde müşterilerden beklenen satın almaları tahmin ediniz ve exp_sales_6_month olarak cltv dataframe'ine ekleyiniz.
           # 2. Gamma-Gamma modelini fit ediniz. Müşterilerin ortalama bırakacakları değeri tahminleyip exp_average_value olarak cltv dataframe'ine ekleyiniz.
           # 3. 6 aylık CLTV hesaplayınız ve cltv ismiyle dataframe'e ekleyiniz.
                # b. Cltv değeri en yüksek 20 kişiyi gözlemleyiniz.
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions
cltv.dtypes
cltv["frequency"]
cltv["recency_cltv_weekly"]
#cltv["frequency"]= cltv["frequency"].astype(int)
#cltv["monetary_cltv_avg"]= cltv["monetary_cltv_avg"].astype(int)
cltv["recency_cltv_weekly"] = cltv["recency_cltv_weekly"].asfreq("D")

bg_nbd = BetaGeoFitter(penalizer_coef=0.01)
bg_nbd.fit(cltv["frequency"],cltv["recency_cltv_weekly"],cltv["T_weekly"])
cltv["exp_sales_3_month"]=bg_nbd.predict(12,cltv["frequency"],cltv["recency_cltv_weekly"],cltv["T_weekly"])
cltv["exp_sales_6_month"]=bg_nbd.predict(24,cltv["frequency"],cltv["recency_cltv_weekly"],cltv["T_weekly"])
#GAMMA
ggf= GammaGammaFitter(penalizer_coef=0.01)
ggf.fit(cltv["frequency"],cltv["monetary_cltv_avg"])
cltv["exp_average_value"]=ggf.conditional_expected_average_profit(cltv["frequency"],cltv["monetary_cltv_avg"])

#6 aylık cltv

cltv["cltv"] =ggf.customer_lifetime_value(bg_nbd,cltv["frequency"],cltv["recency_cltv_weekly"],cltv["T_weekly"],cltv["monetary_cltv_avg"], time = 6, freq="W",discount_rate=0.01)
cltv["cltv"].
cltv=cltv.reset_index()
cltv.head()
# GÖREV 4: CLTV'ye Göre Segmentlerin Oluşturulması
           # 1. 6 aylık tüm müşterilerinizi 4 gruba (segmente) ayırınız ve grup isimlerini veri setine ekleyiniz. cltv_segment ismi ile dataframe'e ekleyiniz.
           # 2. 4 grup içerisinden seçeceğiniz 2 grup için yönetime kısa kısa 6 aylık aksiyon önerilerinde bulununuz
cltv["cltv_segment"] = pd.qcut(cltv["cltv"],4,labels=["D","C","B","A"])


# BONUS: Tüm süreci fonksiyonlaştırınız.

def create_cltv_df(dataframe):

    # Veriyi Hazırlama
    columns = ["order_num_total_ever_online", "order_num_total_ever_offline", "customer_value_total_ever_offline","customer_value_total_ever_online"]
    for col in columns:
        replace_with_thresholds(dataframe, col)

    dataframe["order_num_total"] = dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]
    dataframe["customer_value_total"] = dataframe["customer_value_total_ever_offline"] + dataframe["customer_value_total_ever_online"]
    dataframe = dataframe[~(dataframe["customer_value_total"] == 0) | (dataframe["order_num_total"] == 0)]
    date_columns = dataframe.columns[dataframe.columns.str.contains("date")]
    dataframe[date_columns] = dataframe[date_columns].apply(pd.to_datetime)

    # CLTV veri yapısının oluşturulması
    dataframe["last_order_date"].max()  # 2021-05-30
    analysis_date = dt.datetime(2021, 6, 1)
    cltv_df = pd.DataFrame()
    cltv_df["customer_id"] = dataframe["master_id"]
    cltv_df["recency_cltv_weekly"] = ((dataframe["last_order_date"] - dataframe["first_order_date"]).astype('timedelta64[D]')) / 7
    cltv_df["T_weekly"] = ((analysis_date - dataframe["first_order_date"]).astype('timedelta64[D]')) / 7
    cltv_df["frequency"] = dataframe["order_num_total"]
    cltv_df["monetary_cltv_avg"] = dataframe["customer_value_total"] / dataframe["order_num_total"]
    cltv_df = cltv_df[(cltv_df['frequency'] > 1)]

    # BG-NBD Modelinin Kurulması
    bgf = BetaGeoFitter(penalizer_coef=0.001)
    bgf.fit(cltv_df['frequency'],
            cltv_df['recency_cltv_weekly'],
            cltv_df['T_weekly'])
    cltv_df["exp_sales_3_month"] = bgf.predict(4 * 3,
                                               cltv_df['frequency'],
                                               cltv_df['recency_cltv_weekly'],
                                               cltv_df['T_weekly'])
    cltv_df["exp_sales_6_month"] = bgf.predict(4 * 6,
                                               cltv_df['frequency'],
                                               cltv_df['recency_cltv_weekly'],
                                               cltv_df['T_weekly'])

    # # Gamma-Gamma Modelinin Kurulması
    ggf = GammaGammaFitter(penalizer_coef=0.01)
    ggf.fit(cltv_df['frequency'], cltv_df['monetary_cltv_avg'])
    cltv_df["exp_average_value"] = ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                                                           cltv_df['monetary_cltv_avg'])

    # Cltv tahmini
    cltv = ggf.customer_lifetime_value(bgf,
                                       cltv_df['frequency'],
                                       cltv_df['recency_cltv_weekly'],
                                       cltv_df['T_weekly'],
                                       cltv_df['monetary_cltv_avg'],
                                       time=6,
                                       freq="W",
                                       discount_rate=0.01)
    cltv_df["cltv"] = cltv

    # CLTV segmentleme
    cltv_df["cltv_segment"] = pd.qcut(cltv_df["cltv"], 4, labels=["D", "C", "B", "A"])

    return cltv_df

cltv_df = create_cltv_df(df)


cltv_df.head(10)


