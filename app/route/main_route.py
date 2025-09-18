from app.route import main_bp
from app.service.main_service import main_service

from flask import request, jsonify
@main_bp.route('/', methods=['POST'])
def main_req():
    # Langkah 1: Ambil seluruh dictionary dari JSON
    data_json = request.get_json()

    # Langkah 2: Ekstrak nilai string menggunakan key 'question'
    pertanyaan_teks = data_json['question']
    user_id = data_json['user_id']
    if user_id == None:
        return jsonify(message='user id kosong'),400

    # Kirim variabel string ke service Anda
    return main_service(pertanyaan_teks, user_id)