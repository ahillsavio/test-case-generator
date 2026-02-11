from crewai import LLM

def get_llm():
    
    return LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0.2,
    )
