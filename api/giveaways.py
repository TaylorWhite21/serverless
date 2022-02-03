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
      print(url)
      r = requests.get(url)
      data = r.json()
      games = []
      for game_data in data:
        giveaways = game_data['title']['platforms']['open_giveaway_url']['status']
        games.append(giveaways)
      message = str(games)
    else:
      message = ('Please provide a valid platform')
  
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return























# url_path = self.path
#     url_components = parse.urlsplit(url_path)
#     query_string_list = parse.parse_qsl(url_components.query)
#     dic = dict(query_string_list)

#     if "word" in dic:
#         url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
#         r = requests.get(url + dic['word'])
#         data = r.json()
#         definitions = []
#         for word_data in data:
#             definition = word_data["meanings"][0]["definitions"][0]["definition"]
#             definitions.append(definition)
#         message = str(definitions)        
#     else:
#         message = "Please give me a word to define"

#     self.send_response(200)
#     self.send_header('Content-type', 'text/plain')
#     self.end_headers()

#     self.wfile.write(message.encode())

#     return
