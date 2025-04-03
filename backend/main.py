from fastapi import FastAPI
from agents.regulation_lookup_agent import regulation_lookup_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Financial Compliance AI is Running"}

@app.post("/query-regulation/")
async def query_regulation(question: str):
    response = await regulation_lookup_agent.request("query", {"question": question})
    return {"answer": response["answer"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
