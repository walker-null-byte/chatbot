from urllib.request import urlopen
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError
import pyaudio as pa
import requestAPI
import random 
from threading import Thread
from time import sleep

def randomStringId():
    string=''
    for i in range(5):
        string+=chr(random.randint(50,100))
    return string

def checkInternet():
    try:
        url=urlopen('http://www.google.com/')
        return True
    except:
        return False

def coderunner():
    print('CODERUNNER STARTED\n')
    sleep(50)
    ID = randomStringId()
    mic = Recognizer()
    print()
    print('############################################################')
    print("Chatbot is live, say something...")
    print('############################################################')
    print()
    with Microphone() as source:
        while(True):
            try:
                audio = mic.listen(source, timeout=3)
            except:
                continue
            print("\n")
            if checkInternet(): 
                try:
                    decodedAudio = mic.recognize_google(audio)
                    print("--> "+decodedAudio)
                    requestAPI.messageBot(ID,decodedAudio)
                    
                except UnknownValueError:
                    print("\nGoogle Speech Recognition could not understand audio\n")

                except RequestError as e:
                    print("\nCould not request results from Google Speech Recognition service; {0}\n".format(e))
            else:
                print("You are offline!")
                print("Fetching offline results...")
                try:
                    decodedAudio = mic.recognize_sphinx(audio)
                    requestAPI.messageBot(ID,decodedAudio)
                except UnknownValueError:
                    print("Sphinx Speech Recognition could not understand audio")
                except RequestError as e: 
                    print("Could not request results from Sphinx Speech Recognition service; {0}".format(e))

def main():
    Thread(target=requestAPI.rasaStart).start()
    Thread(target=coderunner).start()

if __name__=='__main__':
    main()
    
