from sqlalchemy import or_
from app.db_model.model_db import Produk, Type, WarantyDetail, Stok
def find_products_by_question(question: str):
    """
    Cari produk relevan berdasarkan pertanyaan user + ambil stok.
    """
    # --- 1. Preprocessing sederhana ---
    text = question.lower()
    keywords = text.split()

    # --- 2. Build query dengan JOIN ke Type dan Stok ---
    query = (
        Produk.query
        .join(Type)
        .outerjoin(Stok)  # pakai outerjoin supaya tetap dapat produk walau stok kosong
    )

    filters = []
    for kw in keywords:
        filters.extend([
            Produk.product_name.ilike(f"%{kw}%"),
            Produk.description.ilike(f"%{kw}%"),
            Produk.garansi.ilike(f"%{kw}%"),
            Type.type_name.ilike(f"%{kw}%")
        ])

    if filters:
        query = query.filter(or_(*filters))

    products = query.all()

    # --- 3. Buat output yang mencakup stok ---
    result = []
    for p in products:
        result.append({
            "product_id": p.product_id,
            "product_name": p.product_name,
            "description": p.description,
            "garansi": p.garansi,
            "harga": float(p.harga),
            "type": p.type.type_name if p.type else None,
            "stok": p.stok[0].kuantitas if p.stok else 0  # akses stok jika ada
        })

    return result


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