from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print("URL loaded:", repr(SUPABASE_URL))   # debug line
print("KEY loaded:", repr(SUPABASE_KEY)[:20], "...")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/tracks/sample")
def get_sample_tracks():
    response = supabase.table("tracks").select("*").limit(5).execute()
    return response.data