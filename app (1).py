import streamlit as st
import pandas as pd

# === Tampilan Styling ===
st.set_page_config(page_title="PharmaBeauty", page_icon="✨", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #FAF3E0;
    }
    .stTextInput, .stSelectbox, .stButton {
        border-radius: 10px;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: grey;
    }
    </style>
""", unsafe_allow_html=True)

# === Judul Aplikasi ===
st.title("🌿 PharmaBeauty - Skincare Guide")
st.write("Cari tahu informasi tentang skincare yang aman dan cocok untuk kamu! 💖")

# === Pilihan Dataset ===
datasets = {
    "Interaksi Bahan Skincare": "interaksi_bahan_skincare(1)(1).csv",
    "Jenis Kulit & Skincare": "jenis_kulit_skincare.csv",
    "Perawatan Ibu Hamil": "perawatan_ibu_hamil(1).csv",
    "Perawatan Kulit Berdasarkan Usia": "perawatan_kulit_usia.csv"
}

selected_dataset = st.sidebar.selectbox("📂 Pilih Dataset:", list(datasets.keys()), key="dataset_selector")
df = pd.read_csv(datasets[selected_dataset])

# === Search Bar ===
st.subheader("🔍 Cari Informasi Skincare")
search_column = st.selectbox("Pilih Kolom untuk Pencarian:", df.columns, key="column_selector")
search_query = st.text_input("Masukkan kata kunci untuk mencari informasi:", "", key="search_bar")

# === Hasil Pencarian ===
if search_query:
    filtered_df = df[df[search_column].astype(str).str.contains(search_query, case=False, na=False)]
    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            st.write("---")
            for col in df.columns:
                st.write(f"**{col}:** {row[col]}")
    else:
        st.warning("❌ Tidak ditemukan hasil yang cocok!")
else:
    st.info("🔎 Masukkan kata kunci untuk mencari informasi skincare!")

# === Footer ===
st.markdown('<p class="footer">Made with 💖 by Diva</p>', unsafe_allow_html=True)
