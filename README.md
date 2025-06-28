📖 Pencari Ayat Al-Qur'an (Berbasis AI)
Aplikasi Streamlit berbasis Gemini 1.5 Flash yang membantu pengguna menemukan ayat-ayat Al-Qur’an berdasarkan tema atau konsep tertentu menggunakan pencarian semantik (berbasis makna).

🚀 Fitur Utama
🔍 Pencarian Berdasarkan Tema: Temukan ayat-ayat Al-Qur’an berdasarkan topik, makna, atau kata kunci semantik.

💡 Respons AI Kontekstual: Didukung oleh model Gemini untuk memahami konteks input pengguna.

📜 Output Terstruktur: Menampilkan Surah, Ayat, terjemahan, dan penjelasan singkat relevansi ayat.

🌐 Antarmuka Sederhana: Dibangun menggunakan Streamlit untuk antarmuka pengguna yang mudah digunakan.


🧠 Teknologi yang Digunakan
Streamlit – UI Framework

Google Generative AI (Gemini) – Model AI untuk pencarian semantik

python-dotenv – Untuk menjaga keamanan API key (alternatif lokal)

⚙️ Cara Menjalankan
bash
Salin
Edit
streamlit run nama_file.py
Pastikan API Key sudah tersedia di st.secrets["API_KEY"].

🧪 Contoh Input
"Ayat tentang bersyukur kepada Allah"
"Keadilan dalam Islam"
"Larangan memakan riba"
"Kesabaran Nabi Ayub"

🛡️ Keamanan
✅ Tidak ada hardcode API Key
✅ Gunakan st.secrets atau .env (tidak di-commit ke GitHub)
✅ File .env sudah disarankan masuk .gitignore

👨‍💻 Tentang Pembuat
Dibuat oleh Haikal Abror
Mahasiswa Informatika & Pengembang Web dengan minat pada NLP & EduTech.

📜 Lisensi
MIT License. Bebas digunakan untuk keperluan pendidikan dan non-komersial.
Sertakan atribusi jika menggunakan atau mengembangkan lebih lanjut dari repositori ini.
