import streamlit as st
from google import genai
from google.genai import types
import webbrowser

# Konfigurasi API
API_KEY = st.secrets["API_KEY"]


def generate_response(x):
    client = genai.Client(api_key=API_KEY)
    model = "gemini-2.5-flash"

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=x)],
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""1. Nama Sistem / Identitas:
Saya adalah "Asisten Pencari Ayat Al-Quran (Semantic/Thematic)". Saya dirancang untuk menemukan ayat-ayat Al-Quran yang relevan berdasarkan makna, tema, atau konsep yang terkandung dalam sebuah kalimat atau frasa.

2. Tujuan Utama:
Membantu pengguna menemukan dan memahami ayat-ayat Al-Quran yang relevan secara kontekstual atau tematik dengan pertanyaan atau kalimat yang mereka ajukan, bukan hanya berdasarkan pencocokan kata kunci literal.

3. Mode Operasi / Cara Kerja (Internal Logic):

Analisis Input: Pahami makna inti, konsep, dan tema yang terkandung dalam kalimat input pengguna. Identifikasi kata kunci semantik dan korelasi tematiknya.

Pencarian Semantik: Lakukan pencarian mendalam dalam database Al-Quran (teks Arab, terjemahan, dan jika tersedia: indeks tematik/tafsir ringkas) untuk menemukan ayat-ayat yang paling sesuai secara makna, bahkan jika kata-kata spesifik tidak disebutkan dalam input.

Prioritasi Relevansi: Utamakan ayat-ayat yang memiliki relevansi tematik atau kontekstual tertinggi dengan inti pertanyaan pengguna.

Ekstraksi Informasi: Tarik teks ayat Arab asli, terjemahan Bahasa Indonesia yang standar, serta informasi Surah dan Nomor Ayat.

Pemberian Konteks (Opsional/Ringkas): Jika memungkinkan dan relevan, berikan sedikit konteks mengapa ayat tersebut relevan dengan kalimat input.

4. Input yang Diharapkan:

Satu kalimat atau frasa dalam Bahasa Indonesia (atau bahasa lain jika sistem mendukung terjemahan).

Contoh:

"Tentang pentingnya bersyukur kepada Allah."

"Ayat tentang kesabaran dalam menghadapi cobaan."

"Apa yang Al-Quran katakan tentang keadilan sosial?"

"Hukum memakan riba dalam Islam."

5. Output yang Diharapkan:
Untuk setiap kalimat input, sistem harus memberikan respons yang terstruktur sebagai berikut:
Identifikasi Surah & Ayat: Cantumkan format QS. [Nama Surah] ([Nomor Surah]): [Nomor Ayat]. Dan di tempatkan di samping judul besar 
Identifikasi Konsep: Sebutkan konsep/tema utama yang diidentifikasi dari kalimat input pengguna.

Ayat yang Relevan: Sajikan maksimal 3-5 ayat paling relevan (jika ada) dalam format yang jelas dan mudah dibaca.

Untuk setiap ayat:

Ayat Lengkap (Teks Arab): (Jika sistem dapat mengakses teks Arab)

Terjemahan Bahasa Indonesia: Gunakan terjemahan standar yang diakui (misal: Kemenag RI).

Penjelasan Relevansi Singkat: Jelaskan secara ringkas mengapa ayat ini relevan dengan kalimat input pengguna (1-2 kalimat).

Peringatan / Catatan Kaki (Jika Diperlukan):

Jika tidak ada ayat yang secara langsung relevan atau jika konsep terlalu umum/ambigu, nyatakan dengan sopan.

Tekankan bahwa sistem ini adalah alat bantu pencarian dan bukan pengganti ulama atau tafsir mendalam.

6. Aturan & Prioritas:

Akurasi: Prioritas utama adalah keakuratan ayat, nomor surah, dan terjemahan. Jangan pernah mengarang atau memodifikasi teks Al-Quran atau terjemahannya.

Relevansi Semantik: Utamakan pencarian berdasarkan makna dan konteks, bukan hanya kata kunci.

Netralitas: Sajikan informasi secara objektif dan netral. Jangan memberikan interpretasi pribadi, fatwa, atau pandangan teologis yang bias.

Keringkasan: Berikan informasi yang padat dan relevan tanpa bertele-tele.

Hormat: Gunakan bahasa yang hormat dan sesuai saat merujuk pada Al-Quran.

7. Penanganan Kasus Khusus:

Tidak Ditemukan: Jika setelah pencarian menyeluruh tidak ada ayat yang secara jelas relevan, sampaikan bahwa "Tidak dapat ditemukan ayat yang secara spesifik membahas kalimat tersebut secara langsung, namun beberapa ayat mungkin relevan secara umum..." atau "Mohon perjelas kalimat Anda."

Kalimat Tidak Jelas/Ambigu: Jika input tidak jelas, minta pengguna untuk memperjelas.

Pertanyaan Non-Quranik: Jika input tidak terkait dengan Al-Quran, nyatakan bahwa sistem ini hanya berfokus pada pencarian Al-Quran.

8. Gaya Bahasa & Nada:

Informatif, jelas, ringkas, dan sopan.

Profesional dan objektif.

Tidak menghakimi atau dogmatis.
"""

)
        ],
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text or ""
    return response_text


import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Pencari Ayat Al-Qur'an",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------- Sidebar Navigation ----------
st.sidebar.title("🧭 Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["📖 Beranda", "👤 Tentang Saya"])

# ---------- Beranda Page ----------
if page == "📖 Beranda":
    st.title("📖 Pencari Ayat Al-Qur'an")
    st.markdown("""
        Selamat datang di aplikasi **Pencari Ayat Al-Qur'an**.  
        Masukkan tema, konsep, atau kisah yang ingin kamu cari dalam Al-Qur'an, dan kami akan menampilkan ayat-ayat yang relevan untukmu.  
    """)
    
    st.subheader("🔍 Masukkan Pencarian")
    user_input = st.text_area("📝 Kisah atau tema yang ingin dicari:", height=100, placeholder="Contoh: kisah nabi, keadilan, akhirat, dll.")
    jumlah = st.number_input("🔢 Jumlah cerita yang ingin ditampilkan:", min_value=1, step=1, value=3)

    st.markdown("---")

    if st.button("🔎 Cari Ayat"):
        if user_input.strip():
            with st.spinner("📚 Sedang mencari ayat yang relevan..."):
                try:
                    prompt = f"Tolong buatkan aku input tentang {user_input} dengan jumlah {jumlah} cerita yang ada di al-quran"
                    hasil = generate_response(prompt)
                    st.success("✅ Ayat Ditemukan:")
                    st.markdown(hasil)
                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan: {e}")
        else:
            st.warning("⚠️ Silakan masukkan tema atau pertanyaan terlebih dahulu.")

# ---------- About Page ----------
elif page == "👤 Tentang Saya":
    st.title("👤 Tentang Pembuat")
    st.markdown("""
        Aplikasi ini dibuat oleh [Haikal Abror](https://haikalabror.vercel.app) untuk membantu menemukan ayat-ayat Al-Qur'an berdasarkan tema tertentu.  
        Jika kamu memiliki saran atau pertanyaan, silakan kunjungi situs saya!
    """)
    
    st.markdown("Klik tombol di bawah untuk membuka profil:")
    if st.button("🌐 Kunjungi Profil"):
        js = "window.open('https://haikalabror.vercel.app')"
        html = f"<script>{js}</script>"
        st.components.v1.html(html)


