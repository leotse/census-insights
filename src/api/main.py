from dataclasses import dataclass
from typing import List, Optional

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from api_models import LngLat
from services.dissemination_area import query_dissemination_area_by_lnglats
from services.stats import query_stats_by_ids, query_stats_by_lnglats

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/dissemination-areas-by-lnglats")
def get_dissemination_area(lnglats: List[LngLat]):
    return query_dissemination_area_by_lnglats(lnglats)


@app.get("/api/stats-by-ids")
def read_stats(dissemination_area_ids: List[str] = Query([])):
    return query_stats_by_ids(dissemination_area_ids)


@app.post("/api/stats-by-lnglats")
def read_stats(lnglats: List[LngLat]):
    return query_stats_by_lnglats(lnglats)
