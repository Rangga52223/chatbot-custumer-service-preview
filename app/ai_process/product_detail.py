from app.llm.ollama_init import call_llm_no_retrive
import json
from app.helper.find_prod import find_products_by_question
from app.helper.saving_chat import save_chat

def product_detail(question, language, user_id):
    product = find_products_by_question(question)
    detail_produk = ""
    for p in product:
        detail_produk += f"""
Nama Produk: {p.product_name}
Deskripsi: {p.description or '-'}
Garansi: {p.garansi or '-'}
Harga: Rp.{p.harga or '-'}
stok: Rp.{p.stok or '-'}
Jenis Produk: {p.type.type_name}
-------------------------------
"""
    prompt = f'''Kamu adalah customer support untuk platform toko online. 
Tugas kamu menjawab pertanyaan dari pelanggan dan jawab seperti chatbot.
Pertanyaan: {question}
Bahasa: {language}
Data produk: 
{detail_produk}
⚠️ Penting:
- Jangan tambahkan penjelasan di luar JSON.
- Hanya keluarkan JSON valid.
Contoh format output:
{{
"jawaban": "jawaban dari pertanyaan tidak boleh dalam bentuk list"
}}'''

    data = call_llm_no_retrive(prompt)
    print("RAW RESPONSE:", data)

    try:
        parsed = json.loads(data) if isinstance(data, str) else data
    except Exception as e:
        print("JSON Parse Error:", e)
        return "Maaf, terjadi kesalahan dalam memproses jawaban."

    jawaban = (parsed.get('jawaban') or '').strip()
    save_chat(user_id, question, jawaban)
    return jawaban

