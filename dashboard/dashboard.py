import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


dingling_df = pd.read_csv("main_data.csv")

dingling_df['date'] = pd.to_datetime(dingling_df[['year', 'month', 'day']])

st.header('Visualisasi Data Polusi Udara Stasiun Dingling 2013-2017 :sparkles:')

st.sidebar.header('Filter Data')
# Filter berdasarkan tanggal
start_date = st.sidebar.date_input("Pilih Tanggal Mulai", value=dingling_df['date'].min())
end_date = st.sidebar.date_input("Pilih Tanggal Akhir", value=dingling_df['date'].max())
filtered_df = dingling_df[(dingling_df['date'] >= pd.Timestamp(start_date)) & (dingling_df['date'] <= pd.Timestamp(end_date))]

polutan_options = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
selected_polutan = st.sidebar.multiselect("Pilih Polutan", options=polutan_options, default=polutan_options)

stasiun_options = dingling_df['station'].unique()
selected_stasiun = st.sidebar.selectbox("Pilih Stasiun", options=stasiun_options)

if 'product' in dingling_df.columns:
    product_options = dingling_df['product'].unique()
    selected_product = st.sidebar.selectbox("Pilih Produk", options=product_options)
    filtered_df = filtered_df[filtered_df['product'] == selected_product]

filtered_df = filtered_df[filtered_df['station'] == selected_stasiun]

filtered_df = filtered_df[['date', 'year', 'month', 'day', 'station'] + selected_polutan]

st.subheader('Konsentrasi Tiap Polutan per Tahun Pada Stasiun Dingling ')
Polutan_dataByYears = filtered_df.groupby('year')[selected_polutan].mean().reset_index()

sns.set(style='whitegrid')
plt.figure(figsize=(12, 6))
for polutan in selected_polutan:
    sns.barplot(x='year', y=polutan, data=Polutan_dataByYears, label=polutan, alpha=0.6)
plt.title('Perbandingan Rata-rata Konsentrasi Tiap Polutan per Tahun Pada Stasiun Dingling')
plt.xlabel('Tahun')
plt.ylabel('Konsentrasi Polutan (µg/m³)')
plt.legend()
plt.grid(True)
st.pyplot(plt)

if 'CO' in selected_polutan:
    st.subheader('Visualisasi Tren Konsentrasi CO Berdasarkan Tahun Pada Stasiun Dingling')
    COByYears = filtered_df.groupby('year')['CO'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='year', y='CO', data=COByYears, marker='o', color='green')
    plt.title('Rata-rata Konsentrasi CO Berdasarkan Tahun Pada Stasiun Dingling')
    plt.xlabel('Tahun')
    plt.ylabel('Konsentrasi CO (ppm)')
    plt.grid(True)
    st.pyplot(plt)

st.subheader('Trend Polusi Udara di Tiap Hari Per Bulannya Pada Stasiun Dingling (2013-2017)')
DayGrouping = filtered_df.groupby("day")[selected_polutan].mean().reset_index()
plt.figure(figsize=(10, 6))
for polutan in selected_polutan:
    plt.plot(DayGrouping.index, DayGrouping[polutan], label=polutan)
plt.xlabel("Hari")
plt.ylabel("Konsentrasi Tiap Polutan dalam microgram/m3")
plt.title("Trend Polusi Udara di Tiap Hari Per Bulannya Pada Stasiun Dingling (2013-2017)")
plt.legend()
plt.grid(True)
st.pyplot(plt)
