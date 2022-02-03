from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  
  def do_GET(self):
    # self.send_response(200)
    # self.send_header('Content-type', 'text/plain')
    # self.end_headers()
    # message = 'Hello World!' 
    # self.wfile.write(message.encode())
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    # GET https://www.gamerpower.com/api/giveaways?platform=pc
    if "platforms" in dic:
      url = 'https://www.gamerpower.com/api/giveaways'
      r = requests.get(url + dic['platforms'])
      print(r)
      data = r.json()
      # giveaways = []
      # for game_data in data:
      #   giveaways = 
      print(data)
