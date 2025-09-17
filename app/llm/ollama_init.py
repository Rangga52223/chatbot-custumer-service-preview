from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from app.helper.json_cleaner import safe_json_parse
import json
import sys

# Inisialisasi model LLM yang menunjuk ke Ollama
# Model yang digunakan adalah llama3.2 versi 3 miliar parameter
llm = Ollama(model="llama3.2:3b")

def call_llm_no_retrive(prompt: str):
    try:
        response = llm.invoke(prompt)

        # Ambil teks
        response_text = getattr(response, "content", str(response)).strip()

        # Bersihkan markdown
        if response_text.startswith("```"):
            response_text = response_text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()

        # Parse aman
        return safe_json_parse(response_text)

    except Exception as e:
        print(f"[Ollama Error] {e}", file=sys.stderr)
        return None
    
def llm_call_tooling(func_name, prompt):
    funct_status_tool = Tool(
        name="CekStatusPesanan",
        func=func_name,
        description="Gunakan tool ini untuk mengecek status pesanan berdasarkan transaction_id"
    )
    agent = initialize_agent(
        tools=[funct_status_tool],
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    query = prompt
    response = agent.run(query) 
    return response   
    
# def call_llm_with_RAG(prompt: str, retriever=None):
#     """
#     Function Execution LLM yang membutuhkan RAG
#     """
#     try:
#         final_prompt = prompt
#         if retriever:
#             # Bagian ini melakukan PENCARIAN
#             docs = retriever.invoke(prompt)
#             context = "\n\n".join([d.page_content for d in docs])
#             final_prompt = f"""
# Jawablah HANYA berdasarkan konteks dan full berikut
# Jika jawaban tidak ada di konteks, jawab dengan "Maaf, saya tidak menemukan informasi tersebut dalam data."

# Konteks:
# {context}

# Pertanyaan: {prompt}
#             """.strip()

#         # --- Kirim ke LLM ---
#         response = llm.invoke(final_prompt)

#         # Ambil teks dari response
#         response_text = (
#             str(response.content).strip() if hasattr(response, "content") else str(response).strip()
#         )

#         # Bersihkan kalau dibungkus codeblock markdown
#         if response_text.startswith("```"):
#             response_text = (
#                 response_text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
#             )

#         # Coba parse JSON
#         try:
#             return json.loads(response_text)
#         except json.JSONDecodeError:
#             return response_text

#     except Exception as e:
#         print(f"[Ollama Error] {e}", file=sys.stderr)
#         return None


# def call_llm_for_product(retriever=None, prompt=None, use_retriever: bool = False):
#     """
#     Kirim prompt ke Ollama (llama3.2:3b). 
#     Jika use_retriever=True, jalankan RAG dengan data DB.
#     """
#     try:
#         if use_retriever:
#             # Buat QA Chain
#             db_prod = SQLDatabase(
#                 engine=db.engine, 
#                 include_tables=["produk", "type"]
#             )
#             toolkit = SQLDatabaseToolkit(db=db_prod, llm=llm)
#             qa_chain = RetrievalQA.from_chain_type(
#                 llm=llm,
#                 toolkit=toolkit,
#                 retriever=retriever,
#                 return_source_documents=True
#             )
#             response = qa_chain.invoke(prompt)
#             response_text = response["result"]

#         else:
#             # Mode normal (tanpa retriever)
#             response = llm.invoke(prompt)

#             if hasattr(response, "content"):
#                 response_text = str(response.content).strip()
#             else:
#                 response_text = str(response).strip()

#             if response_text.startswith("```"):
#                 response_text = response_text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()

#         # Parse ke JSON jika bisa
#         try:
#             return json.loads(response_text)
#         except json.JSONDecodeError:
#             return response_text

#     except Exception as e:
#         print(f"[LLM Error] {e}", file=sys.stderr)
#         return None
    
# def call_llm_with_sql(prompt: str, tables: list[str]):
#     """
#     Kirim prompt ke LLM (Ollama) + SQL Database.
#     - prompt: pertanyaan natural language
#     - tables: daftar tabel yang boleh diakses
#     - db_uri: koneksi DB (default: electric_store lokal)
    
#     Return: string atau JSON (jika valid).
#     """
#     try:
#         # Koneksi DB hanya ke tabel tertentu
#         db = SQLDatabase.from_uri(Config.SQLALCHEMY_DATABASE_URI, include_tables=tables)

#         toolkit = SQLDatabaseToolkit(db=db, llm=llm)

#         agent_executor = create_sql_agent(
#             llm=llm,
#             toolkit=toolkit,
#             agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#             verbose=True,
#             handle_parsing_errors=True
#         )

#         # Jalankan query via LLM
#         response = agent_executor.invoke({"input": prompt})

#         # Ambil teks dari hasil
#         if isinstance(response, dict) and "output" in response:
#             response_text = str(response["output"]).strip()
#         else:
#             response_text = str(response).strip()

#         # Bersihkan jika ada codeblock markdown
#         if response_text.startswith("```"):
#             response_text = response_text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()

#         # Coba parse ke JSON
#         try:
#             return json.loads(response_text)
#         except json.JSONDecodeError:
#             return response_text

#     except Exception as e:
#         print(f"[SQLAgent Error] {e}", file=sys.stderr)
#         return None