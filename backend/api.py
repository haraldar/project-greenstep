from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import redis
import sqlite3

app = FastAPI()
redisDb = redis.Redis(host="localhost", port=6379, decode_responses=True)
con = sqlite3.connect("./greenstep_db.sqlite3")
cur = con.cursor()

# tables (required)
# CREATE TABLE profiles (id TEXT, name TEXT, evee_count NUMBER)


class Credentials(BaseModel):
    username: str
    password: str

class ProfileCreate(BaseModel):
    name: str
    password: str

class ProfileUpdate(BaseModel):
    name: Optional[str]
    evee_count: Optional[int]

class Profile(BaseModel):
    id: str
    name: str
    evee_count: int

class GeoPosition(BaseModel):
    long: float
    lat: float

class SquatCount(BaseModel):
    timestamp: str
    count: int

class CityCheckpoint(BaseModel):
    id: str
    name: str

# login routes

@app.post("/login/")
async def login(credentials: Credentials) -> str:
    return "token"

@app.post("/logout/")
async def logout(token: str) -> None:
    return

# profile routes

@app.get("/profile/{profile_id}")
async def get_profile(profile_id: str) -> Profile:
    pass

@app.post("/profile/create/")
async def create_profile(profile_to_create: ProfileCreate) -> Profile:

    # Check if username exists.
    if cur.execute("SELECT * FROM profiles WHERE id = ?", (profile_to_create.name, )).fetchone():
        return HTTPException(405)

    # Generate new ID.
    new_profile_id = str(uuid.uuid4())
    
    # Save to SQLite DB.
    cur.execute(
        "INSERT INTO profiles (id, name, evee_count, password) VALUES (?, ?, 0, ?)",
        (new_profile_id, profile_to_create.name, profile_to_create.password))
    
    con.commit()

    return {
        "id": new_profile_id,
        "name": profile_to_create.name,
        "evee_count": 0
    }

@app.patch("/profile/update/{profile_id}")
async def update_profile(profile_id: str, profile_to_update: ProfileUpdate) -> Profile:
    pass

# current stats routes

@app.get("/stats/current_city")
async def get_stats_current_city():
    return

@app.get("/stats/total_cities")
async def get_stats_total_cities():
    return

# current geolocation route

@app.get("/geolocation/{profile_id}")
async def get_geolocation(profile_id: str) -> GeoPosition:
    redisDb.hgetall(f"geoloc_{profile_id}")

@app.post("/geolocation/{profile_id}")
async def update_geolocation(profile_id: str, position: GeoPosition):
    redisDb.hset(f"geoloc_{profile_id}", mapping={ "lat" : position.lat, "long" : position.long })

# activities

@app.post("/squat_completed/{profile_id}")
async def completed_squat(profile_id: str):
    squats_count = redisDb.get(f"squats_{profile_id}")
    if not squats_count:
        redisDb.set(f"squats_{profile_id}", 1, ex=60)
    else:
        if int(squats_count) > 19:
            redisDb.delete(f"squats_{profile_id}")
            # get the evee count of the user
            evee_count = cur.execute("SELECT evee_count FROM profiles WHERE id = ?", (profile_id, )).fetchone()[0]
            # increase the users evee_count
            if type(evee_count) == int:
                new_evee_count = int(evee_count) + 1
                cur.execute("UPDATE profiles SET evee_count = ? WHERE id = ?", (new_evee_count, profile_id, ))
                con.commit()
        else:
            redisDb.set(f"squats_{profile_id}", int(squats_count) + 1)

@app.get("/total_squats_completed/{profile_id}")
async def get_total_completed_squats(profile_id: str):
    return {
        "total_squats_completed": redisDb.get(f"squats_{profile_id}")
    }

@app.post("/city_checkpoint_found/{profile_id}")
async def found_city_checkpoint(city_checkpoint: CityCheckpoint):
    return

# evees routes

# @app.post()
# async def gift_evees():

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
