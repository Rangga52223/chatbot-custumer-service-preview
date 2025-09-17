from app.llm.ollama_init import call_llm_no_retrive
from app.ai_process.product_detail import product_detail
from app.ai_process.waranty_explainer import waranty_explainer
from app.ai_process.transaction_tracking import tracking_transaction
from flask import jsonify

def main_service(question):
    if question == None:
        return jsonify(jawaban='tidak ada pertanyaan')
    try:
        prompt = f"""
        Kamu adalah asisten yang hanya memberikan output dalam format JSON valid.

        Tugas:
        1. Perbaiki semua typo pada pertanyaan berikut: "{question}".
        2. Tentukan bahasa pertanyaan tersebut.
        3. Tentukan alur berdasarkan aturan berikut:
        - Jika pertanyaan terkait produk, set "alur" ke "a".
        - Jika pertanyaan terkait garansi, detail garansi, set "alur" ke "b".
        - Jika pertanyaan terkait memasukkan order, transaksi, bukti transaksi, cek status transaksi, set "alur" ke "c".
        ⚠️ Penting:
        - Jangan tambahkan penjelasan di luar JSON.
        - Hanya keluarkan JSON valid.
        Contoh format output:
        {{
        "question": "pertanyaan yang sudah diperbaiki",
        "language": "bahasa pertanyaan",
        "alur": "nomor alur"
        }}
        """
        data = call_llm_no_retrive(prompt)
        print(data)
        alur = (data.get('alur') or '').strip()
        language = (data.get('language') or '').strip()
        question = (data.get('question') or '').strip()
        if alur == 'a':
            jawaban = product_detail(question, language)
            return jsonify(jawaban=jawaban)
        elif alur == 'b':
            return waranty_explainer(question, language)
        elif alur == 'c':
            return tracking_transaction(question, language)
        else:
            return jsonify(jawaban='Pertanyaan mu tidak di ketahui')
    except Exception as e:
        return jsonify(Error=str(e)),400