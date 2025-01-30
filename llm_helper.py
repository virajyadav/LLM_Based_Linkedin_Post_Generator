from dotenv import load_dotenv
from langchain_groq import ChatGroq
from ollama import chat
from ollama import ChatResponse
import os 
load_dotenv()



llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="deepseek-r1-distill-llama-70b",
    temperature=0.0,
)


def chat_with_ollama(model, prompt):
    response = chat(model=model, messages=list(prompt))
    return response.content

if __name__ == "__main__":
    # response = llm.invoke("What is the capital of France?")
    # print(response.content)
    response = chat_with_ollama("deepseek-r1:1.5b", [{'content':'What is the capital of France?'}])
    print(response)