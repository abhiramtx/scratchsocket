import os
os.system("pip uninstall websocket --y")
os.system("pip install websocket-client")
import json
import requests
import re
import logging
import time
import math
import websocket


class scratch:
  def __init__(self, username: str, password: str) -> None:
    global uname
    uname = username
    self.username = username
    self.password = password
    self.headers = {
      "x-csrftoken": "a",
      "x-requested-with": "XMLHttpRequest",
      "Cookie": "scratchcsrftoken=a;scratchlanguage=en;",
      "referer": "https://scratch.mit.edu",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    }
    try:
      data = json.dumps({
        "username": username,
        "password": password
      })
      request = requests.post(
        'https://scratch.mit.edu/login/', data=data, headers=self.headers)
      self.sessionId = re.search(
        '\"(.*)\"', request.headers['Set-Cookie']).group()
      self.token = request.json()[0]["token"]
      headers = {
        "x-requested-with": "XMLHttpRequest",
        "Cookie": "scratchlanguage=en;permissions=%7B%7D;",
        "referer": "https://scratch.mit.edu",
      }
      request = requests.get(
        "https://scratch.mit.edu/csrf_token/", headers=headers)
      self.csrftoken = re.search(
        "scratchcsrftoken=(.*?);", request.headers["Set-Cookie"]).group(1)
      global sessionId
      sessionId = self.sessionId
      global csrftoken
      csrftoken = self.csrftoken
      global token
      token = self.token

    except AttributeError:
      raise Exception(
        'Error: Inputted credentials are invalid!')
    else:
      self.headers = {
        "x-csrftoken": self.csrftoken,
        "X-Token": self.token,
        "x-requested-with": "XMLHttpRequest",
        "Cookie": "scratchcsrftoken="
                  + self.csrftoken
                  + ";scratchlanguage=en;scratchsessionsid="
                  + self.sessionId
                  + ";",
        "referer": "",
      }

  class connect:
    def __init__(self, pid: int):
      global ws
      ws = websocket.WebSocket()
      global PROJECT_ID
      self.username = uname
      PROJECT_ID = pid
      ws.connect('wss://clouddata.scratch.mit.edu', cookie='scratchsessionsid=' + sessionId + ';',
                 origin='https://scratch.mit.edu', enable_multithread=True)
      ws.send(json.dumps({
        'method': 'handshake',
        'user': self.username,
        'project_id': str(pid)
      }) + '\n')

      global chars
      chars = [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        " ",
        "a",
        "A",
        "b",
        "B",
        "c",
        "C",
        "d",
        "D",
        "e",
        "E",
        "f",
        "F",
        "g",
        "G",
        "h",
        "H",
        "i",
        "I",
        "j",
        "J",
        "k",
        "K",
        "l",
        "L",
        "m",
        "M",
        "n",
        "N",
        "o",
        "O",
        "p",
        "P",
        "q",
        "Q",
        "r",
        "R",
        "s",
        "S",
        "t",
        "T",
        "u",
        "U",
        "v",
        "V",
        "w",
        "W",
        "x",
        "X",
        "y",
        "Y",
        "z",
        "Z",
        "*",
        "/",
        ".",
        ",",
        "!",
        '"',
        "§",
        "$",
        "%",
        "_",
        "-",
        "(",
        "´",
        ")",
        "`",
        "?",
        "new line",
        "@",
        "#",
        "~",
        ";",
        ":",
        "+",
        "&",
        "|",
        "^",
        "'"
      ]

      self.current_var = 1
      self.req = []

      print("\033[1mIf you use scratchsocket in your project, please credit @Air_heads!\033[0m")

    def set_var(self, variable: str, value: str):
      try:
        ws.send(json.dumps({
          'method': 'set',
          'name': '☁ ' + variable,
          'value': str(value),
          'user': self.username,
          'project_id': str(PROJECT_ID)
        }) + '\n')
      except Exception: #BrokenPipeError, etc
        logging.error('Broken Pipe Error. Connection Lost.')
        time.sleep(0.1)  # rate limit
        ws.connect('wss://clouddata.scratch.mit.edu', cookie='scratchsessionsid=' + sessionId + ';',
                   origin='https://scratch.mit.edu', enable_multithread=True)
        ws.send(json.dumps({
          'method': 'handshake',
          'user': self.username,
          'project_id': str(PROJECT_ID)
        }) + '\n')
        logging.info('Re-connected to wss://clouddata.scratch.mit.edu')
        logging.info('Re-sending the data')
        ws.send(json.dumps({
          'method': 'set',
          'name': '☁ ' + variable,
          'value': str(value),
          'user': self.username,
          'project_id': str(PROJECT_ID)
        }) + '\n')

    def get_cloud_logs(self, project_id, *, filter_by_var_named=None, limit=25, offset=0):
      try:
        response = json.loads(requests.get(
          f"https://clouddata.scratch.mit.edu/logs?projectid={project_id}&limit={limit}&offset={offset}").text)
        if filter_by_var_named is None:
          return response
        else:
          return list(filter(lambda k: k["name"] == "☁ " + filter_by_var_named, response))
      except Exception:
        return []

    def _encode(self, thing):
      thing = str(thing)
      output = ""
      for i in thing:
        if i in chars:
          output = f"{output}{chars.index(i)}"
        else:
          output += str(chars.index(" "))
      return output

    def _decode(self, thing):
      try:
        thing = str(thing)
      except Exception:
        raise Exception("Invalid decode input!")
      output = ""
      for i in range(0, math.floor(len(thing) / 2)):
        char = chars[int(f"{thing[i * 2]}{thing[(i * 2) + 1]}")]
        output = f"{output}{char}"
      return output

    # REQUESTS
    def request(self, function):
      self.req.append(function)

    def event(self, function):
      if function.__name__ == "on_ready":
        self.on_ready = function

    def _respond(self, request_id, response, limit):
      print("respond")
      remaining_response = str(response)
      i = 0
      while not remaining_response == "":
        if len(remaining_response) > limit:
          response_part = remaining_response[:limit]
          remaining_response = remaining_response[limit:]
          i += 1
          if i > 9:
            part_index = str(i)
          else:
            part_index = "0" + str(i)
          self.set_var(f"FROM_HOST_{self.current_var}", f"{response_part}.{request_id}{part_index}1")
          self.current_var += 1
          if self.current_var == 6:
            self.current_var = 1
          time.sleep(0.1)
        else:
          self.set_var(f"FROM_HOST_{self.current_var}", f"{remaining_response}.{request_id}2222")
          self.current_var += 1
          if self.current_var == 6:
            self.current_var = 1
          remaining_response = ""
          time.sleep(0.1)

    def run(self):
      self.last_data = self.get_cloud_logs(PROJECT_ID, limit=100)
      self.last_timestamp = 0

      data = self.get_cloud_logs(PROJECT_ID, limit=100)
      if data == []:
        pass
      else:
        self.last_timestamp = data[0]["timestamp"]

      try:
        self.on_ready()
      except AttributeError:
        pass

      if self.req == []:
        print("WARNING: No requests found!")

      while True:
        data = self.get_cloud_logs(PROJECT_ID, limit=100)
        if data == []:
          continue
        data.reverse()
        if not self.last_data == data:
          for activity in data:
            if activity['timestamp'] > self.last_timestamp and activity['name'] == "☁ TO_HOST":
              try:
                raw_request, request_id = activity["value"].split(".")
              except Exception:
                self.last_timestamp = activity['timestamp']
                continue
              r = self._decode(raw_request)
              arguments = r.split("§")
              r = arguments.pop(0)
              outp = ""
              commands = list(filter(lambda k: k.__name__ == r, self.req))
              if len(commands) == 0:
                print(f"Warning: Client received an unknown request called '{r}'")
                self._respond(request_id, self._encode(f"Error: Unknown request sent to server"), 220)
              else:
                try:
                  if len(arguments) == 0:
                    outp = commands[0]()
                  elif len(arguments) == 1:
                    outp = commands[0](arguments[0])
                  elif len(arguments) == 2:
                    outp = commands[0](arguments[0], arguments[1])
                  else:
                    print(f"Error: Request '{r}' failed to parse.")
                    outp = self._encode(f"Error: Request '{r}' failed to parse.")
                except Exception as e:
                  self._respond(request_id, self._encode(f"Error: Check the Python console"), 220)
                  print(f"Caught error in request '{r}': {e}")

              if not isinstance(outp, list):
                outp = self._encode(outp)
              else:
                input = outp
                outp = ""
                for i in input:
                  outp += self._encode(i)
                  outp += "89"

              self._respond(request_id, outp, 220)
              self.last_timestamp = activity['timestamp']
          self.last_data = data