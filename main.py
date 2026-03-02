import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/models")
async def get_models_proxy(request: Request):
    """
    Proxies GET requests for model lists to bypass CORS.
    """
    try:
        data = await request.json()
        provider = data.get("provider")
        api_key = data.get("api_key")

        if provider == "openrouter":
            url = "https://openrouter.ai/api/v1/models"
            # OpenRouter models list doesn't strictly require a key, 
            # but we pass it if available for consistency.
            headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        elif provider == "venice":
            url = "https://api.venice.ai/api/v1/models"
            if not api_key:
                raise HTTPException(status_code=400, detail="Venice API Key is required to fetch models")
            headers = {"Authorization": f"Bearer {api_key}"}
        else:
            raise HTTPException(status_code=400, detail="Invalid provider")

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, headers=headers)
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.text)
            return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/chat")
async def chat_proxy(request: Request):
    try:
        data = await request.json()
        provider = data.get("provider")
        api_key = data.get("api_key")
        payload = data.get("payload")

        if not api_key:
            raise HTTPException(status_code=400, detail="API Key is missing")

        if provider == "openrouter":
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Emmy World AI"
            }
        elif provider == "venice":
            url = "https://api.venice.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
        else:
            raise HTTPException(status_code=400, detail="Invalid provider")

        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.text)
            return response.json()
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def get_index():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
