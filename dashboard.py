import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("day.csv")  # Sesuaikan dengan nama file yang benar

# Konversi kolom tanggal ke datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Tambahkan kolom tahun dan bulan
df['year'] = df['dteday'].dt.year
df['month'] = df['dteday'].dt.month

# Transformasi kolom 'season'
season_mapping = {
    1: "Semi",
    2: "Panas",
    3: "Gugur",
    4: "Dingin"
}
df["season"] = df["season"].map(season_mapping)

# Transformasi kolom 'weathersit'
weather_mapping = {
    1: "Cerah",
    2: "Berkabut",
    3: "Hujan Ringan",
    4: "Hujan Lebat"
}
df["weathersit"] = df["weathersit"].map(weather_mapping)

# Streamlit UI
st.title("Dashboard Interaktif Bike Sharing")

# Filter berdasarkan tahun
years = df['year'].unique()
selected_year = st.selectbox("Pilih Tahun:", years, index=0)
filtered_df = df[df['year'] == selected_year]

# Pertanyaan 1: Perbandingan cnt berdasarkan season per tahun
st.subheader("Perbandingan Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="season", y="cnt", data=filtered_df, estimator=sum, palette="viridis", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)
st.write("\n\nDari visualisasi yang dihasilkan menggunakan bar chart, maka dapat disimpulkan bahwa pada setiap musim gugur penyewaan sepeda lebih tinggi dibandingkan dengan musim lainnya dan pada setiap musim semi merupakan musim dengan tingkat penyewaan paling rendah dibandingkan dengan musim lainnya. Tingkat penyewaan untuk setiap musim juga meningkat dari pada tahun sebelumnya")


# Pertanyaan 2: Trend penyewaan berdasarkan cuaca
st.subheader("Trend Penyewaan Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="month", y="cnt", hue="weathersit", data=filtered_df, marker="o", ax=ax)
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penyewaan")
plt.xticks(rotation=45)
st.pyplot(fig)
st.write("\n\nDari visualisasi yang dihasilkan menggunakan line chart, maka dapat disimpulkan bahwa tren penyewaan sepeda per tahunnya akan mulai naik di awal tahun, kemudian rentang pada bulan 6-8 merupakan rentang bulan dengan tren penjualan tinggi yang kemudian akan mulai terjadi penurunan tren setelah bulan 8 hingga akhir tahun. Tingkat Penyewaan sangat tinggi ketika cuaca cerah dan sangat rendah ketika hujan ringan")
