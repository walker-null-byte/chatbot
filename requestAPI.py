import requests
import json
import os
from time import sleep
from sys import exit

def rasaStart():
    currentDIR = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
    currentDIR += "/models/"
    print(currentDIR)
    command = 'rasa run --model "{}"'.format(currentDIR)
    os.system(command)
    
def messageBot(sender,message):
    r=requests.post("http://localhost:5005/webhooks/rest/webhook",data=json.dumps({'sender':sender,'message':message}))
    try:
        print("==>"+eval(r.text)[0]["text"])
    except:
        print("==>"+"Sorry, I am not able to understand your message")
def onlineStatus():
    r=requests.post("http://localhost:5005/webhooks/rest/webhook",data=json.dumps({'sender':'Dillu','message': '41 72 65 20 79 6F 75 20 61 6C 69 76 65 3F'}))
    response = eval(r.text)[0]["text"]
    if response == 'I am alive :)':
        print("Rasa has successfully started...")
    else:
        exit()

def main():
    rasaStart()
    onlineStatus()

if __name__=='__main__':
    main()