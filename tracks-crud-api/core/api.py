from ninja import NinjaAPI
from apps.tracks.api import router as tracks_router

api = NinjaAPI(title="Tracks CRUD API",\
               description="A study project with Django + Django Ninja.",\
               version="0.0.1",)

api.add_router("/tracks/", tracks_router,  tags=["Tracks"])
