import fastapi
from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel
import app
import uvicorn
if __name__=="__main__":
    uvicorn.run(app.app,host="localhost",port=8000,reload=True)