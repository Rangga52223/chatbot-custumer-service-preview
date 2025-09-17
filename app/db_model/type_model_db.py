from sqlalchemy.sql import func
from app import db
# Inisialisasi db (biasanya objek db ini diimpor dari file app utama atau file __init__.py)


# class ProductType(db.Model):
#     """
#     Kelas ini adalah representasi dari tabel 'product_types' di database.
#     """
    
#     # Menetapkan nama tabel secara eksplisit
#     __tablename__ = 'type'

#     # Mendefinisikan kolom-kolom tabel
#     type_id = db.Column(db.Integer, primary_key=True)
#     type_name = db.Column(db.String(100), nullable=False)
#     created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

#     def __repr__(self):
#         return f'<ProductType ID: {self.type_id}, Nama: {self.type_name}>'