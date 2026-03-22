from dotenv import load_dotenv
import requests
import os

load_dotenv()

x_api_key = os.getenv("x-api-key")


def image_search(image_url):
    

    if (image_url == None):
        return (0)

    response = requests.get(
        "https://api.openwebninja.com/realtime-lens-data/search", 
        headers={"x-api-key": x_api_key}, 
        params={"url": image_url}
    )

    return response


"""response = image_search("https://raw.githubusercontent.com/debasingghosh143-coder/image_search_helper/main/src/bottle.jpg")
print("\n\n")
print("Response Headers:", response.headers)
print("\n\n")
print(response.text)
print("\n\n")
data = response.json()
print(type(data))
print("\n\n")
print(type(response))
print("\n\n")
print(response.headers["Content-Type"])
print("\n\n")
print(type(response.text))


data = response.json()
with open("src/result.json", "w") as f:
    json.dump(data, f, indent=4)"""
    
#END WITH TUSHAR