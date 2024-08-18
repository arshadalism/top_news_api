from fastapi import FastAPI, HTTPException
import requests
import redis
import os

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    redis_host = os.getenv('REDIS_HOST', 'localhost')
    app.state.redis = redis.Redis(host=redis_host, port=6379, db=0)


@app.get("/top_news/{count}")
async def top_news(count: int):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    count_str = str(count)
    try:
        value = app.state.redis.get(count_str)
        if value is None:
            response = requests.get(url=url)
            if response.status_code == 200:
                top_stories = response.json()[:count]
                app.state.redis.set(count_str, str(top_stories), ex=600)
                return top_stories
        return value
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@app.on_event("shutdown")
async def shutdown_event():
    app.state.redis.close()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("challenge_2:app", reload=True)


