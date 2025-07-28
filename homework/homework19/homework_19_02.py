import os
import sys
import requests
from urllib.parse import urlparse


BASE_URL = "http://127.0.0.1:8080"
UPLOAD_ENDPOINT = f'{BASE_URL}/upload'
IMAGE_ENDPOINT = f'{BASE_URL}/image'
DELETE_ENDPOINT = f'{BASE_URL}/delete'


def upload_image(local_path: str) -> str:

    if not os.path.exists(local_path):
        raise FileNotFoundError(f'File {local_path} not found')

    with open(local_path, "rb") as f:
        resp = requests.post(UPLOAD_ENDPOINT, files={"image": f})
    resp.raise_for_status()
    data = resp.json()
    return data["image_url"]


def get_image_url(filename: str) -> str:

    headers = {"Content-Type": "text"}
    resp = requests.get(f'{IMAGE_ENDPOINT}/{filename}', headers=headers)
    resp.raise_for_status()
    return resp.json()["image_url"]


def download_image_file(filename: str) -> str:

    headers = {"Content-Type": "image"}
    resp = requests.get(f'{IMAGE_ENDPOINT}/{filename}', headers=headers, stream=True)
    resp.raise_for_status()

    out_name = f'downloaded_{filename}'
    with open(out_name, "wb") as out:
        for chunk in resp.iter_content(8192):
            out.write(chunk)
    return out_name


def delete_image(filename: str) -> str:

    resp = requests.delete(f'{DELETE_ENDPOINT}/{filename}')
    resp.raise_for_status()
    return resp.json().get("message", "")


def main():
    try:

        image_url = upload_image("example.jpg")
        print("Uploaded. URL ->", image_url)

        filename = os.path.basename(urlparse(image_url).path)

        text_url = get_image_url(filename)
        print("GET(text). URL ->", text_url)

        local_copy = download_image_file(filename)
        print("Downloaded file: ", local_copy)

        deleted_url = delete_image(filename)
        print("Deleted on server file with name: ", deleted_url)

    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
