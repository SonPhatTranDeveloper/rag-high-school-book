import os

import cloudinary
from cloudinary import cloudinary_url


class ImageConstants:
    IMAGE_FOLDER = "pages"
    IMAGE_FORMAT = "jpg"
    IMAGE_QUALITY = "auto"


def init_cloudinary() -> None:
    """
    Initialize the cloudinary client
    """
    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    )


def get_image_url(file_path: str) -> str:
    """
    Get the image url from the file name

    Args:
        file_path (str): The path of the file

    Returns:
        str: The url of the image
    """
    # Extract the prefix of the file name
    prefix = file_path.split("/")[-1].split(".")[0]

    return cloudinary_url(
        f"{ImageConstants.IMAGE_FOLDER.value}/{prefix}",
        fetch_format=ImageConstants.IMAGE_FORMAT.value,
        quality=ImageConstants.IMAGE_QUALITY.value,
    )
