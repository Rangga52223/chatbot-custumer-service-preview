from sqlalchemy import or_
from app.db_model.product_model_db import Produk, Type, WarantyDetail
def find_products_by_question(question: str):
    """
    Cari produk relevan berdasarkan pertanyaan user.
    """
    # --- 1. Preprocessing sederhana ---
    text = question.lower()

    # bisa ditingkatkan: hapus stopwords, stemming, dsb.
    keywords = text.split()

    # --- 2. Build query ---
    query = Produk.query.join(Type)
    filters = []

    for kw in keywords:
        filters.append(Produk.product_name.ilike(f"%{kw}%"))
        filters.append(Produk.description.ilike(f"%{kw}%"))
        filters.append(Produk.garansi.ilike(f"%{kw}%"))
        filters.append(Type.type_name.ilike(f"%{kw}%"))

    if filters:
        products = query.filter(or_(*filters)).all()
    else:
        products = query.all()

    return products


def find_warranty_by_question(question: str):
    """
    Cari warranty detail berdasarkan produk yang disebut di pertanyaan user.
    """
    text = question.lower()
    keywords = text.split()

    # 1. Cari produk yang relevan
    query = Produk.query.join(Type)
    filters = []
    for kw in keywords:
        filters.append(Produk.product_name.ilike(f"%{kw}%"))
        filters.append(Produk.description.ilike(f"%{kw}%"))
        filters.append(Produk.garansi.ilike(f"%{kw}%"))
        filters.append(Type.type_name.ilike(f"%{kw}%"))

    if filters:
        products = query.filter(or_(*filters)).all()
    else:
        products = []

    if not products:
        return []  # tidak ada produk cocok

    # 2. Ambil type_id dari produk pertama (atau bisa semua kalau banyak)
    type_ids = list({p.product_type for p in products})

    # 3. Ambil warranty detail sesuai type_id
    warranties = WarantyDetail.query.filter(WarantyDetail.type_id.in_(type_ids)).all()

    return warranties