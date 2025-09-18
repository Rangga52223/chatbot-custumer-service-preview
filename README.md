# 🛠 AI Customer Support Service

Sistem AI Agent untuk menjawab pertanyaan pelanggan terkait produk, garansi, transaksi, dan percakapan sebelumnya.  
Agent menggunakan memori berbasis database SQL untuk mengingat chat sebelumnya dan memberikan respons yang konsisten.

---

## 📦 Instalasi & Requirement

### 1. Persiapan Environment Lokal
Pastikan sudah terinstall:
- **Python 3.10+**
- **pip** (package manager)
- **SQL** Seperti mariadb, saya mau aslinya mau pake postgre, tapi mengikuti ketentuan.
- **Ollama** untuk init ke llama 3.2:3b
- **LLAMA3.2:3b** pastikan sudah di pull
- **Langchain_Comunity** pastikan sudah di install
- **Flask** Flask cukup untuk chatbot sederhana, terlebih lagi ada flask_alchemy


### 2. Cara Instalasi
Clone repository dan install dependency:

```bash
git clone https://github.com/username/project-name.git
cd project-name

# (Opsional) Buat virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

```

Jalankan aplikasi:
```bash
python run.py
```

---

## 🗄 Desain Database

**data base saya terdiri dari 7 table.**<br>
seperti gambar dibawah ini:<br>
![image](l.png)<br>
**-Table Produk**
table produk adalah table yang berisi informasi mengenai produk yang akan di tawarkan

**-Table Type**
table type merupakan table yang berisi infromasi tipe barang, kayak mesin cuci, televisi, kulkas.

**-Table Transaction**
table transaction merupakan table yang berisi informasi tentang transaksi yang telah dilakukan.

**-Table Chat_log**
table chatlog merupakan table yang berisi informasi tentang riwayat chat user dengan chatbot, bergunakan untuk memory untuk llm.

**-Table User**
table user merupakan table yang berisi informasi tentang user seperti user_id.

**-Table Waranty_Detail**
table waranty_detail merupakan table yang berisi tentang informasi batasan batasan kerusakan yang dapat di garansi tergantung tipe nya.<br>

Table stok tidak digunakan

## 📚 Library & Framework yang Digunakan



---

## 🧠 Model LLM yang Digunakan

| Komponen          | Model / Service     |
|------------------|-------------------|
| **LLM Core**     | LLAMA 3.2:3b(Lokal) |
| **Prompting**    | Custom prompt untuk klasifikasi `alur` dan pembuatan jawaban |
| **Memori**       | SQL database + retrieval dari 3 chat terakhir |
| **Framwork LLM**       | Langchain |
| **BE**       | Flask |

---

## ❓ Daftar Pertanyaan yang Dapat Dijawab
Perhatian kasih pertanyaan produk seputar televisi, mesin cuci, dan kulkas saja
- **Produk (alur = a):**  
  - "apa saja produk merek A?"
  - "Apa bagus nya produk A, dibanding produk B"
  - "Rekomendasi televisi, yang cocok untuk ruang keluarga?"
  - "Pilihan kulkas yang muat banyak barang tapi murah di kantong?"
- **Garansi (alur = b):**  
  - "garansi produk A berapa tahun"
  - "Saya habis membeli produk A, dan layar pecah, pemakaian masih 1bln apakah bisa claim garansi?"
- **Transaksi (alur = c):**  
  - "status pesanan saya dengan ID 00000000"
  - "Berapa total Pesanan saya dengan ID 000000"
- **pertanyaan diluar konteks (alur = d):**  
  - "nama saya AZ"
  - "siapa nama Saya"
  - "Hallo"

---

## 🛠 Daftar Tool Call

Agent mendukung tool call berikut:
- **product_detail(question, language)** → Mendapatkan detail produk
- **waranty_explainer(question, language)** → Menjelaskan detail garansi
- **tracking_transaction(question, language, user_id)** → Mengecek status transaksi
- **orther_respond(question, language, user_id, chat_data)** → Memberikan jawaban berbasis chat sebelumnya

---

## 🧪 Cara Uji

1. **Simpan chat:**  
   Kirim request:
   ```json
   { "question": "Rekomdasi televisi murah dan bagus?", "user_id": "21ccf5e0-9240-11f0-bbde-0068eb3251c5" }
   ```
## 📄 Lisensi
MIT License – bebas digunakan dan dimodifikasi.
