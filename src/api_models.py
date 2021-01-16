from pydantic import BaseModel


class LngLat(BaseModel):
    lng: float
    lat: float