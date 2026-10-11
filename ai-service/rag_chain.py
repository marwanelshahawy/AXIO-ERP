# ai-service/rag_chain.py
def answer_manager_query(query: str) -> dict:
    # محاكاة لخطوة الـ RAG
    context = "Retrieved financial data from ERP database"
    response = f"Answer to '{query}' using: {context}"
    return {"query": query, "result": response}

if __name__ == "__main__":
    print(answer_manager_query("ما هو إجمالي مبيعات الربع الأول؟"))