from app.llm.ollama_init import llm_call_tooling
from app.db_model.model_db import Transaction, db
from sqlalchemy.orm import Session
from flask import jsonify
from app.helper.saving_chat import save_chat
def tracking_transaction(question, language, user_id):
    prompt = f'''Kamu adalah Kamu adalah customer support untuk platform toko online.
    Tugas kamu cek status pesanan/hal detail yang di tanyakan oleh costumer berdasarkan id.
    pertanyaan:{question}'''
    jawaban = llm_call_tooling(cek_status_pesanan, prompt, "Gunakan tool ini untuk mengecek status pesanan berdasarkan transaction_id")
    save_chat(user_id, question, jawaban)
    return jsonify(message=jawaban),200


# def get_transaction_status(transaction_id: str) -> str:
#     session: Session = db.session
#     trx = session.query(Transaction).filter_by(transaction_id=transaction_id).first()
#     if not trx:
#         return f"Tidak ada transaksi dengan transaction_id {transaction_id}"
#     return f"Status pesanan dengan transaction_id {transaction_id} adalah: {trx.status}"

def cek_status_pesanan(transaction_id: str):
    transaksi = Transaction.query.filter(
        Transaction.transaction_id.ilike(transaction_id)
    ).first()

    if not transaksi:
        return {
            "success": False,
            "message": f"Tidak ada transaksi dengan ID {transaction_id}. Beritahu user untuk cek ulang."
        }

    # Ambil semua detail transaksi
    return {
        "success": True,
        "transaction": {
            "transaction_id": transaksi.transaction_id,
            "status": transaksi.status,
            "order_date": transaksi.order_date.isoformat() if transaksi.order_date else None,
            "shipping_date": transaksi.shipping_date.isoformat() if transaksi.shipping_date else None,
            "delivery_date": transaksi.delivery_date.isoformat() if transaksi.delivery_date else None,
            "customer_name": transaksi.customer_name,
            "shipping_address": transaksi.shipping_address,
            "total_amount": float(transaksi.total_amount) if transaksi.total_amount else None,
            "payment_method": transaksi.payment_method,
            "items": [
                {
                    "product_id": item.product_id,
                    "product_name": item.product_name,
                    "quantity": item.quantity,
                    "price": float(item.price)
                }
                for item in transaksi.items
            ] if hasattr(transaksi, "items") else []
        }
    }