import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
dingling_df = pd.read_csv("main_data.csv")

st.header('Visualisasi Data Polusi Udara Stasiun Dingling 2013-2017 :sparkles:')

st.subheader('Konsentrasi Tiap Polutan per Tahun Pada Stasiun Dingling ')
dingling_df['date'] = pd.to_datetime(dingling_df[['year', 'month', 'day']])
dingling_df['year'] = dingling_df['date'].dt.year
Polutan_dataByYears = dingling_df.groupby('year')[['PM2.5','PM10','SO2','NO2','CO','O3']].mean().reset_index()
sns.set(style='whitegrid')
plt.figure(figsize=(12, 6))
sns.barplot(x='year', y='PM2.5', data=Polutan_dataByYears, color='red', label='PM2.5', alpha=0.6)
sns.barplot(x='year', y='PM10', data=Polutan_dataByYears, color='green', label='PM10', alpha=0.6)
sns.barplot(x='year', y='SO2', data=Polutan_dataByYears, color='blue', label='SO2', alpha=0.6)
sns.barplot(x='year', y='NO2', data=Polutan_dataByYears, color='yellow', label='NO2', alpha=0.6)
sns.barplot(x='year', y='CO', data=Polutan_dataByYears, color='magenta', label='CO', alpha=0.6)
sns.barplot(x='year', y='O3', data=Polutan_dataByYears, color='orange', label='O3', alpha=0.6)
plt.title('Perbandingan Rata-rata Konsentrasi Tiap Polutan per Tahun Pada Stasiun Dingling')
plt.xlabel('Tahun')
plt.ylabel('Konsentrasi Polutan (µg/m³)')
plt.legend()
plt.grid(True)
plt.show()
st.pyplot(plt)

st.subheader('Visualisasi Tren Konsentrasi CO Berdasarkan Tahun Pada Stasiun Dingling')
dingling_df['date'] = pd.to_datetime(dingling_df[['year', 'month', 'day']])
dingling_df['year'] = dingling_df['date'].dt.year
COByYears = dingling_df.groupby('year')['CO'].mean().reset_index()
sns.set(style='whitegrid')
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='CO', data=COByYears, marker='o', color='green')
plt.title('Rata-rata Konsentrasi CO Berdasarkan Tahun Pada Stasiun Dingling')
plt.xlabel('Tahun')
plt.ylabel('Konsentrasi CO (ppm)')
plt.grid(True)
plt.show()
st.pyplot(plt)


st.subheader('Trend Polusi Udara di Tiap Hari Per Bulannya Pada Stasiun Dingling (2013-2017)')
DayGrouping = dingling_df.groupby("day").mean(numeric_only=True).reset_index()
plt.figure(figsize=(10,6))
plt.plot(DayGrouping.index, DayGrouping["PM2.5"], label="PM2.5")
plt.plot(DayGrouping.index, DayGrouping["PM10"], label="PM10")
plt.plot(DayGrouping.index, DayGrouping["SO2"], label="SO2")
plt.plot(DayGrouping.index, DayGrouping["NO2"], label="NO2")
plt.plot(DayGrouping.index, DayGrouping["O3"], label="O3")
plt.xlabel("Hari")
plt.ylabel("Konsentrasi Tiap Polutan dalam microgram/m3")
plt.title("Trend Polusi Udara di Tiap Hari Per Bulannya Pada Stasiun Dingling (2013-2017)")
plt.legend()
plt.show()
plt.show()
st.pyplot(plt)
