from ollama import chat
import time





def chat_with_ollama(query):
    try:
        model = "deepseek-r1:1.5b"
        prompt = [{'role':'user','content':query}]
        response = chat(model=model, messages=list(prompt),stream=True)
        for chunk in response:
            response =  chunk['message']['content']
            time.sleep(0.05)
            yield response
    except Exception as e:
        print(e)

if __name__ == "__main__":
    query = 'What is the capital of France?'
    response = chat_with_ollama(query)
    print(response)