from app.llm.ollama_init import call_llm_no_retrive, llm
from app.ai_process.product_detail import product_detail
from app.ai_process.waranty_explainer import waranty_explainer
from app.ai_process.transaction_tracking import tracking_transaction
from app.ai_process.orther_respons import orther_respond
from app.helper.saving_chat import get_last_three_chats
from flask import jsonify
# from langchain.agents import initialize_agent, Tool
# from langchain.schema import SystemMessage, HumanMessage
def main_service(question, user_id):
    if question == None:
        return jsonify(jawaban='tidak ada pertanyaan')
    data_chat = get_last_three_chats(user_id)
    try:
        prompt = f"""
        Kamu adalah AI yang HANYA mengembalikan output berupa JSON VALID.
        jangan ada "Berikut adalah kembalihan JSON dengan format yang sesuai:" harus clear.
        Riwayat percakapan:
        {data_chat}

        Pertanyaan baru:
        "{question}"

        Tugas kamu:
        1. Perbaiki semua typo pada pertanyaan.
        2. Tentukan bahasa pertanyaan.
        3. Tentukan alur ("alur") dengan aturan berikut:
        - "a" jika pertanyaan tentang produk (spesifikasi, perbandingan, daftar produk)
        - "b" jika pertanyaan tentang garansi
        - "c" jika pertanyaan tentang order, transaksi, status pengiriman
        - "d" jika:
            • pertanyaan merujuk percakapan sebelumnya (contoh: "tadi saya tanya", "lanjut dari yang tadi")
            • pertanyaan berupa sapaan ("halo", "hai", "selamat pagi", dll)
            • pertanyaan di luar konteks toko online (contoh: "cuaca hari ini bagaimana?")
        
        Kembalikan JSON dengan format:
        {{
        "question": "pertanyaan yang sudah diperbaiki",
        "language": "bahasa",
        "alur": "a/b/c/d"
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

# tools = [
#     Tool(
#         name="product_detail",
#         func=product_detail,
#         description="Gunakan jika pertanyaan terkait produk (nama produk, perbandingan produk, spesifikasi)"
#     ),
#     Tool(
#         name="waranty_explainer",
#         func=waranty_explainer,
#         description="Gunakan jika pertanyaan terkait garansi atau detail garansi"
#     ),
#     Tool(
#         name="tracking_transaction",
#         func=tracking_transaction,
#         description="Gunakan jika pertanyaan terkait transaksi, order, status pengiriman"
#     ),
#     Tool(
#         name="orther_respond",
#         func=orther_respond,
#         description="Gunakan jika pertanyaan menyinggung chat sebelumnya atau topik umum"
#     )
# ]

# # --- 2. Buat agent ---

# agent = initialize_agent(
#     tools,
#     llm,
#     agent="zero-shot-react-description",
#     verbose=True
# )

# # --- 3. Main Service dengan LangChain ---
# def main_service(question, user_id):
#     if question is None:
#         return jsonify(jawaban="tidak ada pertanyaan")
    
#     data_chat = get_last_three_chats(user_id)

#     # Prompt ke agent
#     input_data = {
#         "question": question,
#         "user_id": user_id,
#         "chat_data": data_chat,
#         "language": "auto"  # Bisa diganti hasil deteksi bahasa
#     }

#     try:
#         result = agent.run(f"""
#         Pertanyaan: {question}
#         Chat terdahulu: {data_chat}

#         Tentukan tool mana yang harus dipanggil:
#         - product_detail → untuk pertanyaan tentang produk
#         - waranty_explainer → untuk garansi
#         - tracking_transaction → untuk order/transaksi
#         - orther_respond → jika menyebut chat sebelumnya atau pertanyaan umum

#         Berikan hasil dari tool secara langsung.
#         """)
#         return jsonify(jawaban=result)
#     except Exception as e:
#         return jsonify(Error=str(e)), 400