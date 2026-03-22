import mediapipe as mp
import numpy as np
from src.api import lens_search_api
from src.utils import git_image
from src.db import api_usage, state
import json
from src.web import json_to_html
import src.main

def result(crop):

    sha, url, public_link = git_image.upload_image(crop)
    print(public_link)
    print("frame cropped")

    response = lens_search_api.image_search(public_link)
    api_usage.increase_usage() # adds 1 usage
    print("response saved")

    git_image.delete_image(url, sha)
    print("image deleted")


    data = response.json()

    with open("data/json/result.json", "w") as f:
        json.dump(data, f, indent=4)
    
    json_to_html.create_html()
    
    state.change_glow(0)
    state.change_search(1)

#END WITH TUSHAR