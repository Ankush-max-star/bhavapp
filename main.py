
import requests
import json
import datetime
import os

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
BLOG_ID = os.getenv("BLOG_ID")
BLOG_TITLE = os.getenv("BLOG_TITLE")

# Refresh Access Token
def get_access_token():
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    }
    res = requests.post(url, data=data)
    return res.json().get("access_token")

# पोस्ट पब्लिश
def publish_post():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    content = "आजचा बाजारभाव: कांदा - ₹25, बटाटा - ₹30"
    today = datetime.date.today().strftime("%d-%m-%Y")

    post_data = {
        "kind": "blogger#post",
        "title": f"{BLOG_TITLE} - {today}",
        "content": content
    }

    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    res = requests.post(url, headers=headers, data=json.dumps(post_data))

    if res.status_code == 200:
        print("पोस्ट यशस्वीरित्या टाकली गेली.")
    else:
        print("पोस्ट fail झाली:", res.text)

publish_post()
