from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

# class handler(BaseHTTPRequestHandler):
  
#   def do_GET(self):
#     url_path = self.path
#     url_components = parse.urlsplit(url_path)
#     query_string_list = parse.parse_qsl(url_components.query)
#     dic = dict(query_string_list)
#     # GET https://www.gamerpower.com/api/giveaways?platform=pc
#     if "platform" in dic:
#       url = 'https://www.gamerpower.com/api/giveaways'
#       r = requests.get(url + dic['platform'])
#       data = r.json()
#       giveaways = []
#       for game_data in data:
#         giveaways = 

url = "https://gamerpower.p.rapidapi.com/api/giveaways"

querystring = {"platform":"xbox"}

headers = {
    'x-rapidapi-host': "gamerpower.p.rapidapi.com",
    'x-rapidapi-key': "20db20870fmshe463a252e22f924p103b22jsn8088621c31c8"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
