from datetime import datetime
from ninja import Schema, ModelSchema
from typing import Optional
from .models import Track

# https://django-ninja.rest-framework.com/tutorial/django-pydantic/
class TrackSchemaOut(ModelSchema):
    class Config:
        model = Track
        model_fields = "__all__"

class TrackSchemaIn(ModelSchema):
    class Config:
        model = Track
        model_exclude = ['id',]

class TrackSchemaPartialIn(Schema):
    title: Optional[str]
    artist: Optional[str]
    duration: Optional[float]
    last_play: Optional[datetime]

class NotFoundSchema(Schema):
    message: str
