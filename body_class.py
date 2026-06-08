from fastapi import FastAPI,Body
import uvicorn

app=FastAPI()

@app.post("/items/")

async def fun(price:int=Body(...,gt=0)):
    return {"price":price}

if __name__ == "__main__":
    uvicorn.run("body_class:app",host="127.0.0.1",port=8080,reload=True)


#body class is used with post function because we are validating something by passing request body
