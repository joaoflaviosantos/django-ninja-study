from ninja import Router
from .models import Track
from .schema import TrackSchemaIn, TrackSchemaPartialIn, TrackSchemaOut, NotFoundSchema
from typing import List, Optional, Union

router = Router()

# http://localhost:8000/api/tracks?title=Moon
@router.get('/', response=List[TrackSchemaOut], summary="Retrieve a list of all the tracks.")
def tracks(request, title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all()

@router.get('/{track_id}', response={200: TrackSchemaOut, 404: NotFoundSchema}, summary="Retrieve a specific tracks.")
def track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Could not find track"}

@router.post("/", response={201: TrackSchemaOut}, summary="Create a new track.")
def create_track(request, track: TrackSchemaIn):
    saved_track = Track.objects.create(**track.dict())
    return saved_track

@router.put("/{track_id}", response={200: TrackSchemaOut, 404: NotFoundSchema}, summary="Update a specific track.")
def update_track(request, track_id: int, data: TrackSchemaIn):
    try:
        track = Track.objects.get(pk=track_id)
        for attribute, value in data.dict().items():
            setattr(track, attribute, value)
        track.save()
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Could not find track"}

@router.patch("/{track_id}", response={200: TrackSchemaOut, 404: NotFoundSchema}, summary="Partial update on a specific track.")
def partial_update_track(request, track_id: int, data: TrackSchemaPartialIn):
    try:
        track = Track.objects.get(pk=track_id)
        for attribute, value in data.dict(exclude_none=True).items():
            setattr(track, attribute, value)
        track.save()
        updated_track = Track.objects.get(pk=track_id)
        return 200, updated_track
    except Track.DoesNotExist as e:
        return 404, {"message": "Could not find track"}

@router.delete("/{track_id}", response={200: None, 404: NotFoundSchema}, summary="Delete a specific track.")
def delete_track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        track.delete()
        return 200
    except Track.DoesNotExist as e:
        return 404, {"message": "Could not find track"}
