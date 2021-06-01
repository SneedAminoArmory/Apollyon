import amino
import pyfiglet
import colorama
from colorama import Fore, Back, Style
import threading

print(Fore.BLUE)
print(Style.BRIGHT)

Introduction = pyfiglet.figlet_format("Apollyon!", font="colossal")
print(Introduction)
print("Script programed by Sneed.")
print("Have fun (:")

email = input("Bot Email: ")
password = input("Bot Password: ")
client = amino.Client()
client.login(email=email, password=password)
print("Successfully logged into the bot account.")

subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
    print(name, id)

comId = input("Select the Community: ")
sub_client = amino.SubClient(comId=comId, profile=client.profile)
print("Community Selected.")

title = input("Wiki Title: ")
content = input("Wiki Content: ")

def wikispammer():
    while True:
        try:
            sub_client.post_wiki(title=title, content=content, imageList=[open("placeholder.jpg", "rb")])
            print("Wiki Spammed.")
        finally: pass

threads = []

for i in range(1000):
    t = threading.Thread(target=wikispammer)
    t.daemon = False
    threads.append(t)

for i in range(1000):
    threads[i].start()

for i in range(1000):
    threads[i].join()





