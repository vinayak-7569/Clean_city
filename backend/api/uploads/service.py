import os
import shutil
from uuid import uuid4


UPLOAD_DIR = "storage/complaint_images"


def save_image(file):

    extension = file.filename.split(".")[-1]

    filename = f"{uuid4()}.{extension}"

    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return file_path