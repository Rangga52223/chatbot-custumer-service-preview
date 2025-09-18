from app.llm.ollama_init import llm_call_tooling
from app.db_model.model_db import Transaction, db
from sqlalchemy.orm import Session
from flask import jsonify
from app.helper.saving_chat import save_chat
def tracking_transaction(question, language, user_id):
    prompt = f'''Kamu adalah Kamu adalah customer support untuk platform toko online.
    Tugas kamu cek status pesanan berdasarkan id.
    pertanyaan:{question}'''
    jawaban = llm_call_tooling(cek_status_pesanan, prompt)
    save_chat(user_id, question, jawaban)
    return jsonify(message=jawaban),200


def get_transaction_status(transaction_id: str) -> str:
    session: Session = db.session
    trx = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
    if not trx:
        return f"Tidak ada transaksi dengan transaction_id {transaction_id}"
    return f"Status pesanan dengan transaction_id {transaction_id} adalah: {trx.status}"

def cek_status_pesanan(transaction_id: str):
    transaksi = Transaction.query.filter(
        Transaction.transaction_id.ilike(transaction_id)
    ).first()

    if not transaksi:
        return f"Tidak ada transaksi dengan ID {transaction_id}. Beritahu user untuk cek ulang."
    return f"Status pesanan: {transaksi.status}"