import base64
import re
import platform
import os
import requests
import phonenumbers
from colorama import Fore, Back, Style
from pystyle import *

print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install requests -q -q -q")
        import requests
    try:
        from pystyle import *
    except ImportError:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style

elif platform.system().startswith("Windows"):
    try:
        import requests
    except ImportError:
        os.system("python -m pip install requests -q -q -q")
        import requests
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except ImportError:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *

colorama.init()
banner = Center.XCenter(r"""************************************************************
*                                                          *
*                      ──▄▄██████▄▄                        *
*                      ▄██▀▄█▄▄█▄▀██▄                      *
*                      ▀▀▀▄██▀▀██▄▀▀▀                      *
*                      ─▄███─██─███▄                       *
*                      ─█████▄▄█████                       *
*                                                          *
*            MOBILE INFO, LOCATION AND VALIDITY            *
*                                                          *
* Coded By: Machine1337          Improved By: ✖✘✖Dongle✖✘✖ *
*                                                          *
************************************************************
          Note: Enter Country Code and number
                 (example: +1 1112224444)
                          
""")

def is_valid_mobile_number(mobile_number):
    try:
        phone_number = phonenumbers.parse(mobile_number)
        return phonenumbers.is_valid_number(phone_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

def check_number():
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        
        print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
        
        mobile_number = input(Fore.GREEN + '\n[+] Enter Mobile Number: ')
        
        if is_valid_mobile_number(mobile_number):
            message = base64.b64decode(
                'aHR0cHM6Ly9hcGkuYXBpbGF5ZXIuY29tL251bWJlcl92ZXJpZmljYXRpb24vdmFsaWRhdGU/bnVtYmVyPQ=='.encode(
                    'ascii')).decode('ascii')
            url = f"{message}{mobile_number}"
            hello = base64.b64decode('dGdDckRFOVF0QVF4Q1lvNnk4dHprMUdtQTJKbzBYZmI='.encode('ascii')).decode('ascii')
            payload = {}
            headers = {
                "apikey": f"{hello}"
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            if status_code == 200:
                response_json = response.json()
                country_code = response_json["country_code"]
                number = response_json["number"]
                country_name = response_json["country_name"]
                country_prefix = response_json["country_prefix"]
                international_format = response_json["international_format"]
                line_type = response_json["line_type"]
                local_format = response_json["local_format"]
                valid = response_json["valid"]
                location = response_json["location"]
                print(
                    f"Country code: {country_code}\nNumber: {number}\nCountry name: {country_name}\nCountry prefix: {country_prefix}\nInternational format: {international_format}\nLine type: {line_type}\nLocal format: {local_format}\nLocation: {location}\nValid: {valid}")
            else:
                print(Fore.RED + f"Error: {status_code}")
        else:
            print(Fore.RED + '[*] Invalid Mobile Number....')
    except KeyboardInterrupt:
        print(Fore.RED+'\n[*] You Pressed The Wrong Button....')

check_number()
