from dotenv import load_dotenv
import requests
import base64
import os
import cv2

load_dotenv()

# CONFIG
token = os.getenv("git_token")
repo =os.getenv("repo")
file_path = "src/frame.png"
#file_path = "src/bottle.jpg"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}



def upload_image(frame):

    # convert OpenCV frame → PNG buffer
    _, buffer = cv2.imencode(".png", frame)

    # convert buffer → base64
    content = base64.b64encode(buffer).decode()

    url = f"https://api.github.com/repos/{repo}/contents/{file_path}"

    data = {
        "message": "temporary upload",
        "content": content
    }

    r = requests.put(url, json=data, headers=headers)

    sha = r.json()["content"]["sha"]

    public_url = f"https://raw.githubusercontent.com/{repo}/main/{file_path}"

    return sha, url, public_url



def delete_image(url, sha):
    data = {
        "message": "delete temporary image",
        "sha": sha
    }

    requests.delete(url, json=data, headers=headers)


"""def upload_image():
    with open(file_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()

    url = f"https://api.github.com/repos/{repo}/contents/{file_path}"

    data = {
        "message": "temporary upload",
        "content": content
    }

    r = requests.put(url, json=data, headers=headers)
    sha = r.json()["content"]["sha"]

    public_url = f"https://raw.githubusercontent.com/{repo}/main/{file_path}"

    return sha, url, public_url"""
    
    

"""# UPLOAD
sha, url, public_link = upload_image()

print(public_link)"""

"""# WAIT
time.sleep(20)

# DELETE
delete_image(url, sha)

print("Image deleted")"""

#END WITH TUSHAR