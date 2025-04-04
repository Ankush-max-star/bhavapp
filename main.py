
import datetime
import requests
import json
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Blogger Secrets from GitHub Actions
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
BLOG_ID = os.environ['BLOG_ID']

# बाजारभाव मिळवण्यासाठी फंक्शन (उदाहरण)
def get_bazaarbhav():
    today = datetime.date.today().strftime("%d-%m-%Y")
    # येथे तू वेब स्क्रॅपिंग करून बाजारभाव घेऊ शकतो
    return f"{today} चा बाजारभाव:\nकांदा: ₹1800/q\nटमाटर: ₹1000/q\nबटाटा: ₹1500/q"

def create_service():
    creds_data = {
        "token": "",
        "refresh_token": REFRESH_TOKEN,
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scopes": ["https://www.googleapis.com/auth/blogger"]
    }

    creds = Credentials.from_authorized_user_info(info=creds_data)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    service = build('blogger', 'v3', credentials=creds)
    return service

def post_to_blogger():
    service = create_service()
    post_body = {
        "kind": "blogger#post",
        "title": f"आजचा बाजारभाव - {datetime.date.today().strftime('%d-%m-%Y')}",
        "content": get_bazaarbhav()
    }
    posts = service.posts()
    post = posts.insert(blogId=BLOG_ID, body=post_body, isDraft=False).execute()
    print(f"Posted: {post['url']}")

if __name__ == "__main__":
    post_to_blogger()
