# 导入必要的库
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# 初始化FastAPI应用
app = FastAPI(
    title="情感分析API",
    description="基于DistilBERT的情感分析API，返回积极、中性或消极的情感预测",
    version="1.0.0"
)

# 配置CORS中间件，允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源访问
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有HTTP头部
)

# 定义请求和响应数据模型
class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    score: float

# 应用启动时加载模型
@app.on_event("startup")
async def load_model():
    global model, tokenizer
    model_path = "./sentibot"
    tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()
    print("模型加载完成！")

# 情感标签映射
sentiment_mapping = {0: "positive", 1: "neutral", 2: "negative"}

# 单条文本预测接口
@app.post("/predict", response_model=SentimentResponse)
async def predict_sentiment(request: TextRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="请提供文本内容")
    
    try:
        # 文本预处理和模型推理
        inputs = tokenizer(request.text, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        
        # 处理预测结果
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=1)
        predicted_class_id = logits.argmax().item()
        confidence_score = probabilities[0][predicted_class_id].item()
        
        return SentimentResponse(
            text=request.text,
            sentiment=sentiment_mapping[predicted_class_id],
            score=confidence_score
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"预测过程中出错: {str(e)}")

# 健康检查接口
@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# 启动服务器
if __name__ == "__main__":
    uvicorn.run("model_api:app", host="127.0.0.1", port=8000, reload=True) 