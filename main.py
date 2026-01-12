from  fastapi import FastAPI
import uvicorn 
from src.routes.Chat_router import router as chat_router
app = FastAPI()
app.include_router(chat_router)

if __name__ =="__main__":
    uvicorn.run(app,host ="localhost",port = 5000)