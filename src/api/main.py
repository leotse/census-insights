from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.dissemination_area import query_dissemination_area

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/stats")
def read_stats(lat: float, lon: float):
    return {"location": f"{lat},{lon}"}


@app.get("/api/dissemination-area")
def get_dissemination_area(lng: float, lat: float):
    return query_dissemination_area(lng, lat)
