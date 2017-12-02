import requests

def post(content):
    post = requests.post("https://hastebin.com/documents", data=content.encode('utf-8'))
    return "https://hastebin.com/" + post.json()["key"]
