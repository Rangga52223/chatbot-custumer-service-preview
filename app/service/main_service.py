from app.llm.ollama_init import call_llm_no_retrive
from app.ai_process.product_detail import product_detail
from app.ai_process.waranty_explainer import waranty_explainer
from app.ai_process.transaction_tracking import tracking_transaction
from app.ai_process.orther_respons import orther_respond
from app.helper.saving_chat import get_last_three_chats
from flask import jsonify

def main_service(question, user_id):
    if question == None:
        return jsonify(jawaban='tidak ada pertanyaan')
    data_chat = get_last_three_chats(user_id)
    try:
        prompt = f"""
Kamu adalah asisten yang hanya memberikan output dalam **format JSON valid**.

Tugas kamu:
1. Perbaiki semua typo pada pertanyaan berikut: "{question}".
2. Tentukan bahasa pertanyaan tersebut.
3. Tentukan alur ("alur") berdasarkan aturan berikut, dengan urutan prioritas:
   - **Jika pertanyaan secara eksplisit menyebutkan chat sebelumnya** (misal: "tadi saya chat", "sebelumnya saya tanya", "lanjut dari yang tadi"), set "alur" ke "d".
   - Jika pertanyaan terkait produk, set "alur" ke "a".
   - Jika pertanyaan terkait garansi atau detail garansi, set "alur" ke "b".
   - Jika pertanyaan terkait memasukkan order, transaksi, bukti transaksi, atau cek status transaksi, set "alur" ke "c".
   - Jika pertanyaan di luar lingkup a, b, c DAN menanyakan tentang chat terdahulu/masa lalu, set "alur" ke "d".

⚠️ Penting:
- Jangan menambahkan penjelasan di luar JSON.
- Hanya keluarkan **JSON valid**.

Format output yang diharapkan:
{{
    "question": "pertanyaan yang sudah diperbaiki",
    "language": "bahasa pertanyaan",
    "alur": "kode alur (a/b/c/d)"
}}
"""

        data = call_llm_no_retrive(prompt)
        print(data)
        alur = (data.get('alur') or '').strip()
        language = (data.get('language') or '').strip()
        question = (data.get('question') or '').strip()
        if alur == 'a':
            jawaban = product_detail(question, language, user_id)
            return jsonify(jawaban=jawaban)
        elif alur == 'b':
            return waranty_explainer(question, language)
        elif alur == 'c':
            return tracking_transaction(question, language, user_id)
        elif alur == 'd':
            return orther_respond(question, language, user_id, data_chat)
        else:
            return jsonify(jawaban='Pertanyaan mu tidak di ketahui')
    except Exception as e:
        return jsonify(Error=str(e)),400