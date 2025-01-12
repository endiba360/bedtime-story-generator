from fastapi import FastAPI, HTTPException
from app.database import stories_collection
from app.utils import generate_story

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Bedtime Story Generator!"}

@app.post("/generate-story/")
async def generate_story_endpoint(prompt: str):
    story = generate_story(prompt)
    story_data = {"promp": prompt, "story": story}
    stories_collection.insert_one(story_data)
    return {"prompt": prompt, "story": story}