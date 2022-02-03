from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  
  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    # GET https://www.gamerpower.com/api/giveaways?platform=pc
    if 'platforms' in dic:
      url = 'https://www.gamerpower.com/api/giveaways'
      url = url + '?platform=' + dic['platforms']
      r = requests.get(url)
      data = r.json()
      games = []
      for game_data in data:
        giveaways = data['platforms']
        games.append(giveaways)
        message = str(games)
    else:
      message = ('Please provide a valid platform')
  
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return
