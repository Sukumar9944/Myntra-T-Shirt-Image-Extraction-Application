import requests
from PIL import Image
import io

def download_image(url):
    try:
        image_content = requests.get(url).content
        image = io.BytesIO(image_content)

        return image

    except Exception as e:
        print("failed", e)


def view_image(url):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        return image

    except Exception as e:
        print("Please Try Again!", e)