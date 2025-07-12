import requests


def download_mars_photos(sol: int, camera: str, api_key: str = "DEMO_KEY", count: int = 2):
    api_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {"sol": sol, "camera": camera, "api_key": api_key}

    resp = requests.get(api_url, params=params)
    resp.raise_for_status()
    photos = resp.json().get("photos", [])

    if not photos:
        print("No photos found for sol=", sol, "camera=", camera)
        return

    for idx, photo in enumerate(photos[:count], start=1):
        img_url = photo["img_src"]
        print(f"Downloading #{idx} from {img_url}")
        img_resp = requests.get(img_url, stream=True)
        img_resp.raise_for_status()

        filename = f"mars_photo{idx}.jpg"
        with open(filename, "wb") as f:
            for chunk in img_resp.iter_content(8192):
                f.write(chunk)
        print(f"Saved {filename}")


if __name__ == "__main__":
    download_mars_photos(sol=1000, camera="fhaz", api_key="DEMO_KEY", count=2)
    print('All photos have been saved successfully.')
