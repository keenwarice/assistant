import socket
import requests
from urllib.parse import quote

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80), timeout=2)
        return True
    except OSError:
        return False
    
def search_google(question):
    api_key = "" # im obviously not putting my api key here. go to readme.md for instructions on setting this up
    cx="" # also go to readme.py
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={quote(question)}"
    response = requests.get(url)
    if response.status_code==200:
        data=response.json()
        items=data.get("items", [])
        results=[]
        for item in items[:3]: # only give most relevant info with top 3
            title=item.get("title", "an unknown source").replace('"',"'")
            snippet= item.get("snippet","").replace('"',"'")
            results.append(f'accoring to "{title}": "{snippet}"')
        return ", ".join(results)
    else:
        return "There was an error with the search with status code "+response.status_code
