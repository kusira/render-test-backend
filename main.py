from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS の設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # フロントエンドの URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# データモデルの定義
class UserData(BaseModel):
    name: str
    age: int

# POST リクエストエンドポイント
@app.post("/api/process")
async def process_data(user_data: UserData):
    if user_data.age < 0:
        raise HTTPException(status_code=400, detail="Age must be a positive number.")
    
    # データを加工してレスポンスを作成
    response = {
        "message": f"Hello {user_data.name}, you are {user_data.age} years old!",
        "processed": True
    }
    return response

