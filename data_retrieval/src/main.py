from fastapi import FastAPI, HTTPException
from dal import Dal

app = FastAPI()
dal = Dal()


@app.get("/antisemitic")
def get_all_soldiers():
    result = dal.find_all_tweets_antisemitic()
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=500, detail="Database error")
    return result

@app.get("/not_antisemitic")
def get_all_soldiers():
    result = dal.find_all_tweets_not_antisemitic()
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=500, detail="Database error")
    return result