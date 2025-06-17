from langchain_groq import ChatGroq

def get_groq_llm():
    return ChatGroq(
        model="llama3-8b-8192",
        groq_api_key ="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",
        temperature=0.5
    )
