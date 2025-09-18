from app.llm.ollama_init import call_llm_no_retrive
from app.helper.saving_chat import save_chat
from flask import jsonify
def orther_respond(question, language, user_id, chat_data=None):
    prompt = f'''Kamu adalah customer support untuk platform toko online. 
        Data chat terdahulu: {chat_data}.
        Bahasa:{language}
        Pertanyaan:{question}
        Tugas kamu:
        1.jawab pertanyaan dari customer.
        2.ada data data chat terdahulu yang bisa digunakan untuk relevansi
        3.jawab langsung
        contoh : 'ya ini chat yang pernah kamu lakukan'
        Gunakan bahasa yang ramah dan profesional sebagai customer support.'''
    jawaban = call_llm_no_retrive(prompt)
    save_chat(user_id, question, jawaban)
    return jsonify(message=jawaban),200