from app.llm.ollama_init import call_llm_no_retrive
from app.helper.saving_chat import save_chat
from flask import jsonify
def orther_respond(question, language, user_id, chat_data=None):
    prompt = f'''Kamu adalah customer support untuk platform toko online. 
        Data chat terdahulu: {chat_data}
        Tugas kamu:
        1. Jika customer menanyakan chat/percakapan sebelumnya, jawab berdasarkan data chat terdahulu di atas.
        2. Jika customer menyapa (halo, hai, selamat pagi, dll) atau menanyakan identitas kamu, jawab dengan ramah sebagai customer support.
        3. Jika pertanyaan terkait toko online (produk, garansi, transaksi, pengiriman, dll), berikan jawaban yang relevan.
        4. Jika pertanyaan di luar lingkup toko online dan bukan poin 1-2 di atas, jawab bahwa kamu adalah customer support yang hanya bisa membantu hal-hal terkait toko online.
        contoh : 'ya ini chat yang pernah kamu lakukan'
        Gunakan bahasa yang ramah dan profesional sebagai customer support.'''
    jawaban = call_llm_no_retrive(prompt)
    save_chat(user_id, question, jawaban)
    return jsonify(message=jawaban),200