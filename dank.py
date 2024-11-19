#!/usr/bin/python3

import os
import subprocess
import sqlite3
import uuid
import datetime
import base64
import time
from cryptography.fernet import Fernet

dank_database = "dank_memories.db"

while True:
  timestamp = datetime.datetime.now().strftime("%A %d %B %Y, %I:%M:%S.%f %p")
  event = str(uuid.uuid4())
  teh_file = str(event) + '.jpg'
  os_command = 'scrot ' + teh_file
  sub_return = subprocess.run(os_command, shell=True)
  if sub_return.returncode == 0:
    file_binary = open(teh_file, 'rb').read()
    file_base64_utf8_str = base64.b64encode(file_binary).decode('utf-8')
    dataurl_struct = f'data:image/jpg;base64,{file_base64_utf8_str}'
    if len(dataurl_struct) > 0:
      naughty_naughty = "rm -f " + teh_file
      os.system(naughty_naughty)
    else:
      pass
    lolz_key = Fernet.generate_key()
    uber_secure = Fernet(lolz_key).encrypt(dataurl_struct.encode())
    
    con = sqlite3.connect(dank_database)
    cur = con.cursor()
    execute_sql = "INSERT INTO pics_or_it_never_happened VALUES('" + str(event) + "', '" + str(timestamp) + "', '" + str(uber_secure.decode()) + "')"
    cur.execute(execute_sql)
    con.commit()
    time.sleep(1)
    timestamp = datetime.datetime.now().strftime("%A %d %B %Y, %I:%M:%S.%f %p")
    event = str(uuid.uuid4())
    con = sqlite3.connect(dank_database)
    cur = con.cursor()
    execute_sql = "INSERT INTO ephemeral_keys VALUES('" + str(event) + "', '" + str(timestamp) + "', '" + str(lolz_key.decode()) + "')"
    cur.execute(execute_sql)
    con.commit()
  else:
    pass
