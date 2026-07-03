from fastapi import FastAPI
import ollama
import datetime as dt
app = FastAPI()

# constants
MODEL = "llama3.2:latest"
history = [
    {"role": "system", "content": "You are a concise, friendly assistant who talks mostly in UK slang."}
]



@app.get("/")
def welcome():
    return {"message": "Welcome to the Ollama API!"}


@app.get("health-check")
def healthCheck():
    try:
        response = ollama.chat(model=MODEL, messages= history, options={"temperature": 0.3})
        return{"model_repsonse":response["message"]["content"]}
    except Exception as e:
        return {
            "Error": e,
            "Solution": f"Make sure 'ollama server' is running and you ran 'ollama pull {MODEL}'"
            }



# @app.get("/ollama")
# def read_root():
#     return {"Hello": "Ollama API "}

# @app.get("/className")
# def className():
#     return {"className": "Deepseek Emobilis"}


# chat
@app.post("/chat")
def support_chat(message):
    history.append({"role": "user", "content": message})
    response = ollama.chat(
        model=MODEL,
        messages=history,
        options={"temperature": 0.3}
        )["message"]["content"]
    history.append({"role": "assistant", "content": response})
    return {
        "response": response
        }  

@app.get("/history")     
def get_history():
    return {"history": history}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}