from app.route import test_bp
from flask import request
from app.service.test import test
@test_bp.route('/', methods=['POST'])
def test_req():
    # Langkah 1: Ambil seluruh dictionary dari JSON
    data_json = request.get_json()

    # Langkah 2: Ekstrak nilai string menggunakan key 'question'
    pertanyaan_teks = data_json['question']

    # Kirim variabel string ke service Anda
    return test(pertanyaan_teks)