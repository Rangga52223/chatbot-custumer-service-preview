import uuid
from datetime import datetime
from app import db



class Produk(db.Model):
    __tablename__ = "produk"

    product_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    product_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    garansi = db.Column(db.String(50), nullable=True)
    harga = db.Column(db.Numeric(12, 2), nullable=False)
    product_type = db.Column(db.Integer, db.ForeignKey("type.type_id"), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)

    # Relasi ke tabel type
    type = db.relationship("Type", back_populates="products")


class Type(db.Model):
    __tablename__ = "type"

    type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)

    products = db.relationship("Produk", back_populates="type")
    waranty_details = db.relationship("WarantyDetail", back_populates="type")


class WarantyDetail(db.Model):
    __tablename__ = "waranty_detail"   # sesuai tabel di DB

    waranty_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    waranty_detail = db.Column(db.Text, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey("type.type_id"), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)

    type = db.relationship("Type", back_populates="waranty_details")

class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"
    
class Transaction(db.Model):
    __tablename__ = "transaction"

    transaction_id  = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey("user.user_id"), nullable=False)
    id_produk = db.Column(db.String(36), db.ForeignKey("produk.product_id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum("pending", "pengiriman", "selesai", name="status_enum"), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    total_harga = db.Column(db.Numeric(12, 2), default=0.00)

    # --- Relasi ---
    user = db.relationship("User", backref="transactions")
    produk = db.relationship("Produk", backref="transactions")

    def __repr__(self):
        return f"<Transaction {self.log_id} | User {self.user_id} | Produk {self.id_produk}>"
    
class ChatLog(db.Model):
    __tablename__ = "chat_log"

    chat_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey("user.user_id"), nullable=False)
    chat_user = db.Column(db.Text, nullable=False)
    chat_bot = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relasi ke User
    user = db.relationship("User", backref=db.backref("chat_logs", lazy=True))

    def __repr__(self):
        return f"<ChatLog {self.chat_id} - User {self.user_id}>"
    
class Stok(db.Model):
    __tablename__ = "stok"

    id_stok = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_produk = db.Column(db.String(36), db.ForeignKey("produk.product_id"), nullable=False)
    kuantitas = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)

    # Relasi ke Produk
    produk = db.relationship("Produk", backref="stok")

    def __repr__(self):
        return f"<Stok {self.id_stok} | Produk {self.id_produk} | Qty {self.kuantitas}>"
