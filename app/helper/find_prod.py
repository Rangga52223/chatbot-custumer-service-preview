from sqlalchemy import or_
from app.db_model.model_db import Produk, Type, WarantyDetail, Stok
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


def find_product_with_warranty(question: str):
    """
    Cari produk relevan berdasarkan pertanyaan + ambil garansi & waranty_detail.
    Return data siap pakai untuk LangChain tool-calling.
    """
    text = question.lower()
    keywords = text.split()

    query = (
        Produk.query
        .join(Type)
        .join(WarantyDetail, WarantyDetail.type_id == Produk.product_type)
    )

    filters = []
    for kw in keywords:
        filters.extend([
            Produk.product_name.ilike(f"%{kw}%"),
            Produk.description.ilike(f"%{kw}%"),
            Produk.garansi.ilike(f"%{kw}%"),
            Type.type_name.ilike(f"%{kw}%"),
            WarantyDetail.waranty_detail.ilike(f"%{kw}%")
        ])

    if filters:
        query = query.filter(or_(*filters))

    products = query.all()

    result = []
    for p in products:
        result.append({
            "product_id": p.product_id,
            "product_name": p.product_name,
            "description": p.description,
            "harga": float(p.harga),
            "garansi": p.garansi,
            "type": p.type.type_name if p.type else None,
            "waranty_detail": [
                w.waranty_detail for w in p.type.waranty_details
            ] if p.type and p.type.waranty_details else []
        })

    return result
