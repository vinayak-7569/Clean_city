from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from backend.api.uploads.service import (
    save_image
)

router = APIRouter(
    prefix="/upload",
    tags=["Uploads"]
)


@router.post("")
def upload_image(
    file: UploadFile = File(...)
):

    image_path = save_image(file)

    return {
        "image_url": image_path
    }