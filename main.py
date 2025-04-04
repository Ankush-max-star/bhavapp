
import requests
import os

# Blogger API कडून Secrets घेणे
BLOGGER_API_KEY = os.getenv("BLOGGER_API_KEY")
BLOG_ID = os.getenv("BLOG_ID")
BLOG_TITLE = os.getenv("BLOG_TITLE")

# पोस्ट डेटा (इथे तू scraped बाजारभाव टाकू शकतो)
post_data = {
    "kind": "blogger#post",
    "title": f"{BLOG_TITLE}",
    "content": "<p>आजचा बाजारभाव: कांदा - ₹20, बटाटा - ₹25, टोमॅटो - ₹18</p>"
}

# Blogger API URL
url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts?key={BLOGGER_API_KEY}"

# API कॉल करून पोस्ट करणे
response = requests.post(url, json=post_data)

# यशस्वी पोस्ट झाली का ते तपासा
if response.status_code == 200:
    print("✅ आजचा बाजारभाव Blogger वर पोस्ट झाला!")
else:
    print(f"❌ पोस्ट अपलोड करताना त्रुटी आली: {response.text}")
