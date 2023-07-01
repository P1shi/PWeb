import requests
import time
import threading
from os import system

B = '\033[35m'
R = '\033[31m'
N = '\033[0m'
A = '\033[34m'
BB = '\033[36m'

system("cls")

while True:
    print(R + """



   ▄███████▄  ▄█     █▄     ▄████████ ▀█████████▄  
  ███    ███ ███     ███   ███    ███   ███    ███ 
  ███    ███ ███     ███   ███    █▀    ███    ███ 
  ███    ███ ███     ███  ▄███▄▄▄      ▄███▄▄▄██▀  
▀█████████▀  ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀██▄  
  ███        ███     ███   ███    █▄    ███    ██▄ 
  ███        ███ ▄█▄ ███   ███    ███   ███    ███ 
 ▄████▀       ▀███▀███▀    ██████████ ▄█████████▀  
                                                   
╭—————————————————————————————————————————————————╮
|Tool devoloped : P1shi                           |
|Github         : https://github.com/P1shi        |
|Discord        : Pishi  ᵁⱽ#1027                  |
╰—————————————————————————————————————————————————╯
""")
    webhook_url = input(R + "[" + B + "#" + R + "] Webhook URL : ")
    custom_username = input(R + "[" + B + "+" + R + "] " + "Webhook username : ")
    avatar_url = " "
    message_content = input(R + "[" + B + "+" + R + "] " + "Content : ")
    messages_per_sec = input(R + "[" + B + "+" + R + "] " + "Messages per second : ")
    if not messages_per_sec.isdigit():
        print(R + "[" + B + "!" + R + "] " + "Please put a known number in the blank." )
        time.sleep(2)
        print("\033c")
        continue
    messages_per_sec = int(messages_per_sec)
    message = {"content": message_content, "username": custom_username, "avatar_url": avatar_url}

    def send_messages():
        while True:
            for i in range(messages_per_sec):
                response = requests.post(webhook_url, json=message)
                if response.status_code == 204:
                    print(A + "[" + BB + "$" + A + "] " + BB + "1 message successfully sent" )
                elif response.status_code == 429:
                    print(R + "[" + B + "!" + R + "] " + "You are being rate limited " )
                
                elif response.status_code == 404:
                    print(R + "[" + B + "!" + R + "] " + "Invalid webhook url " )
                    time.sleep(4.0)
                    print("\033c")
                    break
            else:
                time.sleep(1)
                continue
            break


    threads = []
    for i in range(messages_per_sec):  
        t = threading.Thread(target=send_messages)
        threads.append(t)
        t.start()


    for t in threads:
        t.join()


    print(R + "[" + B + "!" + R + "] " + " an unknown error occurred\nplease check webhook url or other things.\n Note : remember that webhook url , username , message content and messages per sec are important but webhook profile is optional" )
    time.sleep(3)
    print("\033c")

