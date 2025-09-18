from app.llm.ollama_init import call_llm_no_retrive
import json
from app.db_model.model_db import WarantyDetail
from app.helper.find_prod import find_warranty_by_question
from flask import jsonify

def waranty_explainer(question, language):
    prompt = f'''Tugas kamu memilih alur untuk menetukan pertanyaan garansi.
    -Jika pertanyaan hanya menanyakan detail garansi produk saja tanpa riwayat transaksi maka alur = a 
    -Jika pertanyaan menanyakan garansi berdasarkan struk pembelian maka alur = b
    pertanyaan:{question}
    ⚠️ Penting:
    - Jangan tambahkan penjelasan di luar JSON.
    - Hanya keluarkan JSON valid.
    Contoh format output:
    {{
    alur : "alurnya"
    }}'''
    data = call_llm_no_retrive(prompt)
    print(data)
    alur = (data.get('alur') or '').strip()
    
    if alur == 'a':
        return waranty_prod_explain(question, language)
    elif alur == 'b':
        return jsonify(message='masuk a waranty'),200
    
    else:
       return jsonify(message='saya tidak tahu yang kamu maksud'),200 
    

def waranty_prod_explain(question, languange):
    product = find_warranty_by_question(question)
    detail_warranty = ""
    for p in product:
        # ambil semua warranty detail sesuai type_id produk
        warranties = WarantyDetail.query.filter_by(type_id=p.product_type).all()
        
        # gabungkan semua detail jadi string
        warranty_text = "\n".join([f"- {w.warranty_detail}" for w in warranties]) or "-"

        detail_warranty += f"""
    Nama Produk : {p.product_name}
    Jenis Produk: {p.type.type_name}
    Detail Garansi:
    {warranty_text}
    -------------------------------
    """
    prompt=f'''Kamu adalah Kamu adalah customer support untuk platform toko online.
    Tugas kamu menjawab pertanyaan dari consument berdasarkan data yang saya berikan, dan balas sesuai bahasa yang di berikan.
    Pertanyaan: {question}.
    bahasa:
    data:{detail_warranty}.
    ⚠️ Penting:
    - Jangan tambahkan penjelasan di luar JSON.
    - Hanya keluarkan JSON valid.
    Contoh format output:
    {{
    jawaban : "jawaban"
    }}    '''
    data = call_llm_no_retrive(prompt)
    jawaban = (data.get('jawaban') or '').strip()
    return jsonify(message = jawaban),200
