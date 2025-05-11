from fastapi import FastAPI 
import uvicorn
from routes import user,friends,chat


app = FastAPI(title="Video confrenece application")
app.include_router(user.router)
app.include_router(friends.router)
app.include_router(chat.router)





@app.get("/")
async def heathCheck():
    return "health is mast."

if __name__ =="__main__":
    uvicorn.run( host="0.0.0.0",port=3216,reload=True,app="main:app")