
import requests
import time 
import termcolor
from termcolor import colored
import os 

def main():
    message=input(f"{name}: ")
    data = {
        "content" : message,
        "username" : name,
        "avatar_url" : avatar
    }
    messagesent = requests.post(hook, json = data)
    try:
        messagesent.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(colored(f"Message has been sent, status code: {messagesent.status_code}.", 'magenta'))
        time.sleep(1)
        os.system('cls')
        main()



hook=input("Webhook: ")
if hook.startswith("https://"):
    print("webhook format valid")
    time.sleep(1)
    os.system('cls')
    name=input("Client Name: ")
    avatar=input("Client Avatar[Provide Url]: ")
    print("data stored...")
    time.sleep(2)
    os.system("cls")
    main()
else:
    print(colored("Webhook format invalid", 'red'))
    time.sleep(2)