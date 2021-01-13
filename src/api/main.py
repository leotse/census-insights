from typing import List, Optional

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from models import Session
from services.dissemination_area import query_dissemination_area
from services.stats import query_stats

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/dissemination-area")
def get_dissemination_area(lng: float, lat: float):
    try:
        session = Session()
        return query_dissemination_area(lng, lat, session=session)
    except:
        session.rollback()
        raise
    finally:
        session.close()


@app.get("/api/stats")
def read_stats(dissemination_area_ids: List[str] = Query([])):
    try:
        session = Session()
        return query_stats(dissemination_area_ids, session=session)
    except:
        session.rollback()
        raise
    finally:
        session.close()
