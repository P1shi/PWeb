import requests
from colorama import Fore, Style, init
import time
import threading
import platform
import os

B = '\033[35m'
R = '\033[31m'
N = '\033[0m'
A = '\033[34m'
BB = '\033[36m'

def main():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print(f"""
{R}██████{B}╗ {R}██{B}╗    {R}██{B}╗{R}███████{B}╗{R}██████{B}╗ 
{R}██{B}╔══{R}██{B}╗{R}██{B}║    {R}██{B}║{R}██{B}╔════╝{R}██{B}╔══{R}██{B}╗
{R}██████{B}╔╝{R}██{B}║ {R}█{B}╗ {R}██{B}║{R}█████{B}╗  {R}██████{B}╔╝
{R}██{B}╔═══╝ {R}██{B}║{R}███{B}╗{R}██{B}║{R}██{B}╔══╝  {R}██{B}╔══{R}██{B}╗
{R}██{B}║     {B}╚{R}███{B}╔{R}███{B}╔╝{R}███████{B}╗{R}██████{B}╔╝
╚═╝      ╚══╝╚══╝ ╚══════╝╚═════╝ 
                                  
""")
    try:
        webhook_url = input(f"{R}[{B}+{R}] Webhook URL : {B}")
        print(f"{B}[{A}${B}] Cheking Webhook...")
        time.sleep(1)
        def check_webhook_existence(webhook_url):
            try:
                response = requests.head(webhook_url)
                if response.status_code == 200:
                    return True
                else:
                    return False
            except requests.exceptions.RequestException as e:
                return False

        if check_webhook_existence(webhook_url):
            print(f"{B}[{A}~{B}] Webhook Exists.")
        else:
            print(f"{R}[{B}!{R}] Webhook does not exist.")
            time.sleep(5)
            main()
        custom_username = input(f"{R}[{B}+{R}] Webhook username : {B}")
        avatar_url = ""
        threads_use = input(f"{R}[{B}+{R}] Threads : {B}")
        if not threads_use.isdigit():
            print(f"{R}[{B}!{R}] Please Enter a Valid Number")
            time.sleep(5)
            main()
        message_content = input(f"{R}[{B}+{R}] Content : {B}")
        message = {"content": message_content, "username": custom_username, "avatar_url": avatar_url}

    except:
        print(f"{R}[{B}!{R}] An Unknown Error Occurred.\n\nTip : Maybe You Leave Some Input Blanks")

    def send_messages():
        while True:
            for i in range(50):
                
                response = requests.post(webhook_url, json=message)
                if response.status_code == 204:
                    print(f"{B}[{A}~{B}] {A}» {B} Message Successfully Sent.")
                elif response.status_code == 429:
                    print(f"{R}[{B}!{R}] {B}» {R}You are being rate limited.")
                    time.sleep(7)
                    response = requests.post(webhook_url, json=message)
                elif response.status_code == 404:
                    print(f"{R}[{B}!{R}] {B}» {R}Cant Fing The Webhook.")
            time.sleep(2)


    threads = []
    for i in range(3):  
        t = threading.Thread(target=send_messages)
        threads.append(t)
        t.start()


    for t in threads:
        t.join()


    
main()
