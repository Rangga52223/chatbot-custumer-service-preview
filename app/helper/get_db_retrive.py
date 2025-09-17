from app.db_model.product_model_db import Produk, Type
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma


def build_product_retriever(persist_dir: str = "./chroma_db", use_retriever: bool = True):
    products = Produk.query.join(Type).all()

    if not products:
        print("⚠️ Tidak ada data produk di DB.")
        return None

    docs = []
    for p in products:
        content = f"""
Nama Produk: {p.product_name}
Deskripsi: {p.description or '-'}
Garansi: {p.garansi or '-'}
Jenis Produk: {p.type.type_name}
"""
        docs.append(
            Document(
                page_content=content.strip(),
                metadata={
                    "product_id": p.product_id,
                    "type_name": p.type.type_name,
                    "created_at": str(p.created_at),
                },
            )
        )

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectordb = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)

    if use_retriever:
        return vectordb.as_retriever(search_type="similarity", search_kwargs={"k": len(docs)})
    else:
        # Kembalikan semua dokumen langsung
        return docs