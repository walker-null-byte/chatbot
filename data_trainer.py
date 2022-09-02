from errno import ECHILD
import os
import datetime
from re import T
def main():
    print("Enter name: ")
    name=input()
    date=datetime.datetime.now()

    filename = 'sample_data/{}.txt'.format(name+"_"+date.ctime().replace(" ","_").replace(":","_"))
    os.makedirs(os.path.dirname(filename),exist_ok=True)

    with open(filename,'a') as file:
        while(True):
            question = input("Enter expected ques: ")
            if question=="exit" or question=="Exit":
                break
            answer = input("enter expected answer: ")
            file.write("Question: " + question + "\n")
            file.write("Answer: " + answer)

if __name__=='__main__':
    main()