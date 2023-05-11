from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
   
app = FastAPI()
   
@app.get("/")
async def root():
    return {"He":"Uds"}

@app.get("/1")
async def des():
    file_p="./EXPT1.md"
    return FileResponse(file_p)

@app.get("/3")
async def des():
    file_p="./EXPT3.md"
    return FileResponse(file_p)

@app.get("/4")
async def des():
    file_p="./EXPT4.md"
    return FileResponse(file_p)

@app.get("/5")
async def des():
    file_p="./EXPT5.md"
    return FileResponse(file_p)

@app.get("/6")
async def des():
    file_p="./EXPT6.md"
    return FileResponse(file_p)

@app.get("/7")
async def des():
    file_p="./EXPT7.md"
    return FileResponse(file_p)

@app.get("/8")
async def des():
    file_p="./EXPT8.md"
    return FileResponse(file_p)

@app.get("/9")
async def des():
    file_p="./EXPT9.md"
    return FileResponse(file_p)

@app.get("/10")
async def des():
    file_p="./Expt10.md"
    return FileResponse(file_p)

@app.get("/11")
async def des():
    file_p="./EXPT11.md"
    return FileResponse(file_p)

@app.get("/12")
async def des():
    file_p="./Expt12.md"
    return FileResponse(file_p)
