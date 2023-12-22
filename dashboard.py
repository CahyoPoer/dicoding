import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import calendar

#Fungsi untuk menampilkan data polusi udara
def data_polusi_udara(df, option):
    df['year'] = df['date_time'].dt.year
    df['month'] = df['date_time'].dt.month
    df['day'] = df ['date_time'].dt.day
    df['hour'] = df['date_time'].dt.hour
    df_polusi_udara = df[['year', 'month', 'day', 'hour', 'PM2_5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
    if (option == "per-jam"):
        df_polusi_udara = df.groupby(by = ['year', 'month', 'day','hour'] ).agg({
            "PM2_5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month', 'day','hour'], ascending = True)
        df_polusi_udara = df_polusi_udara.reset_index()
        df_polusi_udara['time'] = df_polusi_udara["hour"].astype(str) + ":00"
    elif (option == "per-hari"):
        df_polusi_udara = df.groupby(by = ['year', 'month', 'day'] ).agg({
            "PM2_5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month', 'day'], ascending = True)
        df_polusi_udara = df_polusi_udara.reset_index()
        df_polusi_udara['time'] = df_polusi_udara["year"].astype(str) + "-" + df_polusi_udara["month"].astype(str) + "-" + df_polusi_udara["day"].astype(str)
    else:
        df_polusi_udara = df.groupby(by = ['year', 'month'] ).agg({
            "PM2_5" : "mean",
            "PM10" : "mean",
            "SO2" : "mean",
            "NO2" : "mean",
            "CO" : "mean",
            "O3" : "mean"}).sort_values(by = ['year', 'month'], ascending = True)
        df_polusi_udara = df_polusi_udara.reset_index()
        df_polusi_udara['time'] = df_polusi_udara["year"].astype(str) + "-" + df_polusi_udara["month"].astype(str)
    return df_polusi_udara

def display_polusi_udara(df):
    pm25= round(df['PM2_5'].mean(), 2)
    pm10= round(df['PM10'].mean(), 2)
    SO2= round(df['SO2'].mean(), 2)
    NO2= round(df['NO2'].mean(), 2)
    CO= round(df['CO'].mean(), 2)
    O3= round(df['O3'].mean(),2)

    with st.container():
        col1, col2, col3 = st.columns([2,1,1])
        with col1:
            st.metric("PM2.5:", value = pm25)
        with col2:
            st.metric("SO2:", value = SO2)
        with col3:
                st.metric("NO2:", value = NO2)

    with st.container():
        col1,col2, col3 = st.columns([2,1,1])
        with col1:
            st.metric("PM10:", value = pm10)
        with col2:
            st.metric("CO:", value = CO)
        with col3:
            st.metric("O3:", value = O3)

def grafik_polusi_udara(df):
    with st.expander("PM2_5"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['PM2_5'], marker='o', linewidth=2, color="Blue")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("PM2.5", fontsize=25)
        ax.set_title("PM2.5", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("PM10"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['PM10'], marker='o', linewidth=2, color="Blue")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("PM10", fontsize=25)
        ax.set_title("PM10", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("SO2"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['SO2'], marker='o', linewidth=2, color="Blue")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("SO2", fontsize=25)
        ax.set_title("SO2", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("NO2"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['NO2'], marker='o', linewidth=2, color="Blue")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("NO2", fontsize=25)
        ax.set_title("NO2", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("CO"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['CO'], marker='o', linewidth=2, color="Blue")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("CO", fontsize=25)
        ax.set_title("CO", loc="center", fontsize=35)
        st.pyplot(fig)

    with st.expander("O3"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['O3'], marker='o', linewidth=2, color="Blue")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("O3", fontsize=25)
        ax.set_title("O3", loc="center", fontsize=35)
        st.pyplot(fig)

#Fungsi untuk menampilkan data perubahan suhu
def data_perubahan_suhu(df, option):
    df['year'] = df['date_time'].dt.year
    df['month'] = df['date_time'].dt.month
    df['day'] = df ['date_time'].dt.day
    df['hour'] =df['date_time'].dt.hour
    df_perubahan_suhu = df[['year', 'month', 'day', 'hour', 'TEMP']]
    if (option == "per-jam"):
        df_perubahan_suhu = df.groupby(by = ['year', 'month', 'day','hour'] ).agg({
            "TEMP" : "mean"}).sort_values(by = ['year', 'month', 'day','hour'], ascending = True)
        df_perubahan_suhu = df_perubahan_suhu.reset_index()
        df_perubahan_suhu['time'] = df_perubahan_suhu["hour"].astype(str) + ":00"
    elif (option == "per-hari"):
        df_perubahan_suhu = df.groupby(by = ['year', 'month', 'day'] ).agg({
            "TEMP" : "mean"}).sort_values(by = ['year', 'month', 'day'], ascending = True)
        df_perubahan_suhu = df_perubahan_suhu.reset_index()
        df_perubahan_suhu['time'] = df_perubahan_suhu["year"].astype(str) + "-" + df_perubahan_suhu["month"].astype(str) + "-" + df_perubahan_suhu["day"].astype(str)
    else:
        df_perubahan_suhu = df.groupby(by = ['year', 'month'] ).agg({"TEMP" : "mean"}).sort_values(by = ['year', 'month'], ascending = True)
        df_perubahan_suhu = df_perubahan_suhu.reset_index()
        df_perubahan_suhu['time'] = df_perubahan_suhu["year"].astype(str) + "-" + df_perubahan_suhu["month"].astype(str)
    return df_perubahan_suhu

def display_perubahan_suhu(df):
    suhu= round(df['TEMP'].mean(), 2)

    with st.container():
        st.metric("SUHU:", value = str(suhu) + " °C")

def grafik_perubahan_suhu(df):
    with st.expander("SUHU"):
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.plot(df['time'], df['TEMP'], marker='o', linewidth=2, color="Blue")
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax.set_ylabel("SUHU (°C)", fontsize=25)
        ax.set_title("SUHU", loc="center", fontsize=35)
        st.pyplot(fig)

#Fungsi menghitung korelasi polusi udara dengan suhu
def korelasi_polusi_udara_dan_suhu(df):
    pm25_suhu = round(df['PM2_5'].corr(df['TEMP']),7)
    pm10_suhu = round(df['PM10'].corr(df['TEMP']),7)
    SO2_suhu = round(df['SO2'].corr(df['TEMP']),7)
    NO2_suhu = round(df['NO2'].corr(df['TEMP']),7)
    CO_suhu = round(df['CO'].corr(df['TEMP']),7)
    O3_suhu = round(df['O3'].corr(df['TEMP']),7)
    correlation_suhu = {'parameter': ["PM2_5", "PM10", "SO2", "NO2", "CO", "O3"],
                        'values' : [pm25_suhu, pm10_suhu, SO2_suhu, NO2_suhu, CO_suhu, O3_suhu]}
    correlation_suhu_df = pd.DataFrame(correlation_suhu)
    correlation_suhu_df

def grafik_korelasi(df):
    with st.expander("Korelasi polusi udara dan suhu"):
        fig1, ax1 = plt.subplots(figsize=(16, 8))
        ax1.scatter(df['TEMP'], df['PM2_5'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax1.tick_params(axis='y', labelsize=20)
        ax1.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax1.set_xlabel("SUHU", fontsize = 20)
        ax1.set_ylabel("PM2.5", fontsize = 20)
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=(16, 8))
        ax2.scatter(df['TEMP'], df['PM10'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax2.tick_params(axis='y', labelsize=20)
        ax2.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax2.set_xlabel("SUHU", fontsize = 20)
        ax2.set_ylabel("PM10", fontsize = 20)
        st.pyplot(fig2)

        fig3, ax3 = plt.subplots(figsize=(16, 8))
        ax3.scatter(df['TEMP'], df['SO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax3.tick_params(axis='y', labelsize=20)
        ax3.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax3.set_xlabel("SUHU", fontsize = 20)
        ax3.set_ylabel("SO2", fontsize = 20)
        st.pyplot(fig3)

        fig4, ax4 = plt.subplots(figsize=(16, 8))
        ax4.scatter(df['TEMP'], df['NO2'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax4.tick_params(axis='y', labelsize=20)
        ax4.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax4.set_xlabel("SUHU", fontsize = 20)
        ax4.set_ylabel("NO2", fontsize = 20)
        st.pyplot(fig4)

        fig5, ax5 = plt.subplots(figsize=(16, 8))
        ax5.scatter(df['TEMP'], df['CO'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax5.tick_params(axis='y', labelsize=20)
        ax5.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax5.set_xlabel("SUHU", fontsize = 20)
        ax5.set_ylabel("CO", fontsize = 20)
        st.pyplot(fig5)

        fig6, ax6 = plt.subplots(figsize=(16, 8))
        ax6.scatter(df['TEMP'], df['O3'],s = 400, alpha = 0.5, c = "#FACE2D",marker = 'o', edgecolors= "#ed7d53")
        ax6.tick_params(axis='y', labelsize=20)
        ax6.tick_params(axis='x', labelsize=20, labelrotation = 45)
        ax6.set_xlabel("SUHU", fontsize = 20)
        ax6.set_ylabel("O3", fontsize = 20)
        st.pyplot(fig6)

#Gathering Data
df_dashboard = pd.read_csv("Data_Kualitas_Udara_dan_Suhu_Changping.csv")
df_dashboard["date_time"] = pd.to_datetime(df_dashboard["date_time"])

#Penentuan batas tanggal input tanggal
min_date = df_dashboard["date_time"].min().date()
max_date = df_dashboard["date_time"].max().date()

#Program Utama
st.title("Kualitas Udara dan Perubahan Suhu di Changping")
with st.sidebar:
    option = st.selectbox("Tampilkan data:", ("per-jam", "per-hari", "per-bulan"))

#Jika memilih data per-jam
if (option == "per-jam") :
    with st.sidebar:
        exact_date = st.date_input(
            label='Tanggal',
            min_value= min_date,
            max_value= max_date,
            value= None,
            format = "YYYY-MM-DD"
        )
        start_time = st.time_input(
            label = "Awal" ,
            value = None,
            step = 3600
        )
        end_time = st.time_input(
            label = "Akhir" ,
            value = None,
            step = 3600
        )
    date_start = str(exact_date) + " " + str(start_time)
    date_end = str(exact_date) + " " + str(end_time)

    df_prog_utama = df_dashboard[(df_dashboard["date_time"].astype(str) >= date_start) & (df_dashboard["date_time"].astype(str) <= date_end)]
    
    df_polusi_udara = data_polusi_udara(df_prog_utama,option)
    df_perubahan_suhu = data_perubahan_suhu(df_prog_utama,option)

    # Visualisasi Data Polusi Udara
    with st.container():
        st.header("Kualitas Udara di Changping")
        display_polusi_udara(df_polusi_udara)
        grafik_polusi_udara(df_polusi_udara)

    # Visualisasi Data Perubahan Suhu
    with st.container():
        st.header("Perubahan Suhu di Changping")
        display_perubahan_suhu(df_perubahan_suhu)
        grafik_perubahan_suhu(df_perubahan_suhu)

    #Visualisasi Korelasi Polusi Udara dan Perubahan Suhu
    with st.container():
        st.header("Korelasi Polusi Udara dan Perubahan Suhu")
        with st.container():
            st.subheader("Tabel korelasi")
            korelasi_polusi_udara_dan_suhu(df_prog_utama)
        with st.container():
            st.subheader("Grafik Scatter")
            grafik_korelasi(df_prog_utama)


#Jika memilih data per-hari
elif (option == "per-hari"):
    with st.sidebar:
    # Mengambil data tanggal untuk dijadikan nilai pivot
        start_date, end_date = st.date_input(
            label='Tanggal',
            min_value= min_date,
            max_value= max_date,
            value= [min_date, max_date]
            )

    date_start = str(start_date) + " 00:00:00"
    date_end = str(end_date) + " 23:00:00"

    df_prog_utama = df_dashboard[(df_dashboard["date_time"].astype(str) >= date_start) & (df_dashboard["date_time"].astype(str) <= date_end)]
    
    df_polusi_udara = data_polusi_udara(df_prog_utama,option)
    df_perubahan_suhu = data_perubahan_suhu(df_prog_utama,option)

    # Visualisasi Data Polusi Udara
    with st.container():
        st.header("Kualitas Udara di Changping")
        display_polusi_udara(df_polusi_udara)
        grafik_polusi_udara(df_polusi_udara)

    # Visualisasi Data Perubahan Suhu
    with st.container():
        st.header("Perubahan Suhu di Changping")
        display_perubahan_suhu(df_perubahan_suhu)
        grafik_perubahan_suhu(df_perubahan_suhu)

    #Visualisasi Korelasi Polusi Udara dan Perubahan Suhu
    with st.container():
        st.header("Korelasi Polusi Udara dan Perubahan Suhu")
        with st.container():
            st.subheader("Tabel korelasi")
            korelasi_polusi_udara_dan_suhu(df_prog_utama)
        with st.container():
            st.subheader("Grafik Scatter")
            grafik_korelasi(df_prog_utama)

#Jika memilih data per-bulan
else:
    with st.sidebar:
    # Mengambil data tanggal untuk dijadikan nilai pivot
        st.text('Data Awal')
        with st.expander('Pilih Bulan dan Tahun'):
            tahun_awal = st.selectbox('tahun awal', range(2013, 2017, 1))
            month_abbr = calendar.month_abbr[1:]
            bulan_awal_str = st.radio('bulan awal', month_abbr, index=1 - 1, horizontal=True)
            bulan_awal = month_abbr.index(bulan_awal_str) + 1 #Jika nanti butuh format date
        st.text(f'{bulan_awal_str}-{tahun_awal} ')

        st.text('Data Akhir')
        with st.expander('Pilih Bulan dan Tahun'):
            tahun_akhir = st.selectbox('tahun akhir', range(2013, 2017, 1))
            month_abbr = calendar.month_abbr[1:]
            bulan_akhir_str = st.radio('bulan akhir', month_abbr, index=1 - 1, horizontal=True)
            bulan_akhir = month_abbr.index(bulan_akhir_str) + 1 #Jika nanti butuh format date
        st.text(f'{bulan_akhir_str}-{tahun_akhir} ')
        

    date_start = str(tahun_awal) + "-" + str(bulan_awal).rjust(2, '0') + "-01 00:00:00"
    date_end = str(tahun_akhir) + "-" + str(bulan_akhir).rjust(2, '0') + "-31 23:00:00"

    df_prog_utama = df_dashboard[(df_dashboard["date_time"].astype(str) >= date_start) & (df_dashboard["date_time"].astype(str) <= date_end)]

    df_polusi_udara = data_polusi_udara(df_prog_utama,option)
    df_perubahan_suhu = data_perubahan_suhu(df_prog_utama,option)

    # Visualisasi Data Polusi Udara
    with st.container():
        st.header("Kualitas Udara di Changping")
        display_polusi_udara(df_polusi_udara)
        grafik_polusi_udara(df_polusi_udara)

    # Visualisasi Data Perubahan Suhu
    with st.container():
        st.header("Perubahan Suhu di Changping")
        display_perubahan_suhu(df_perubahan_suhu)
        grafik_perubahan_suhu(df_perubahan_suhu)

    #Visualisasi Korelasi Polusi Udara dan Perubahan Suhu
    with st.container():
        st.header("Korelasi Polusi Udara dan Perubahan Suhu")
        with st.container():
            st.subheader("Tabel korelasi")
            korelasi_polusi_udara_dan_suhu(df_prog_utama)
        with st.container():
            st.subheader("Grafik Scatter")
            grafik_korelasi(df_prog_utama)

