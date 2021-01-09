from typing import Optional

from fastapi import FastAPI

from services.dissemination_area import query_dissemination_area

app = FastAPI()


@app.get("/api/stats")
def read_stats(lat: float, lon: float):
    return {"location": f"{lat},{lon}"}


@app.get("/api/dissemination-area")
def get_dissemination_area(lat: float, lon: float):
    return query_dissemination_area(lat, lon)
