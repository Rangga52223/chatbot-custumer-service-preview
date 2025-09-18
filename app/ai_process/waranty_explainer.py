from app.llm.ollama_init import llm_call_tooling
from app.helper.find_prod import find_product_with_warranty
from flask import jsonify
import json

def waranty_explainer(question, language):
    prompt = f"""
Kamu adalah asisten yang hanya memberikan output dalam format JSON valid.

Tugas kamu:
1. Evaluasi apakah pertanyaan berikut hanya menanyakan detail garansi produk 
   (misalnya masa garansi, syarat garansi, lama garansi) tanpa menyebut riwayat transaksi.
2. Jika iya, set "is_warranty_question" = true, jika tidak = false.
3. Jangan menambahkan kata lain di luar format JSON.

Pertanyaan: "{question}"

Format output:
{{
    "question": "pertanyaan yang sudah diperbaiki",
    "is_warranty_question": true/false
}}
"""

    # Panggil LLM dengan tool
    answer = llm_call_tooling(
        find_product_with_warranty, 
        prompt, 
        "Gunakan untuk mencari produk berdasarkan pertanyaan user dan mengambil informasi garansi. "
        "Mengembalikan daftar produk lengkap dengan garansi dan waranty_detail."
    )

    try:
        parsed_answer = json.loads(answer)
    except json.JSONDecodeError:
        return jsonify(error="Jawaban dari LLM tidak valid", raw=answer), 500

    if parsed_answer.get("is_warranty_question"):
        # Ambil produk + garansi
        produk_dengan_waranti = find_product_with_warranty(question)
        return jsonify({
            "question": parsed_answer.get("question"),
            "is_warranty_question": True,
            "produk": produk_dengan_waranti
        }), 200
    else:
        return jsonify({
            "question": parsed_answer.get("question"),
            "is_warranty_question": False,
            "message": "Pertanyaan ini tidak hanya tentang detail garansi"
        }), 200



   


