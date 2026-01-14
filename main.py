from  fastapi import FastAPI
import uvicorn 
from src.routes.Chat_router import router as Chat_router
app = FastAPI()
app.include_router(Chat_router)

if __name__ =="__main__":
    uvicorn.run(app,host ="localhost",port = 4001)