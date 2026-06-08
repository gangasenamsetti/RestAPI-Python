from fastapi import FastAPI,Path
import uvicorn

app=FastAPI()

#usage of path in path parameter
@app.get("/validation/{name}")
async def fun(name:str=Path(...,min_length=3,max_length=10)):
    return {"name":name}

if __name__ == "__main__":
   uvicorn.run("parameter_validation:app", host="127.0.0.1", port=8080, reload=True)
