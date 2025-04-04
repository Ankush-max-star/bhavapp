from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import datetime

creds = Credentials(
    token=None,
    refresh_token="YOUR_REFRESH_TOKEN",
    token_uri="https://oauth2.googleapis.com/token",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)

service = build('blogger', 'v3', credentials=creds)

blog_id = "YOUR_BLOG_ID"
today = datetime.datetime.now().strftime("%d-%m-%Y")
title = f"आजचे बाजारभाव - {today}"
content = "सध्या बाजारभाव माहिती अपडेट होत आहे..."

post = {
    "kind": "blogger#post",
    "title": title,
    "content": content
}

request = service.posts().insert(blogId=blog_id, body=post, isDraft=False)
response = request.execute()
print(f"Post published: {response['url']}")
