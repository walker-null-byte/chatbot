from asyncore import write
import datetime
date=datetime.datetime.now()
print(type(date.ctime()))

import os
name = 'DIl'
print('sample_data/{}.txt'.format(name+date.ctime().replace(" ","_")))
dir = 'hem/{}.txt'.format(name+date.ctime().replace(" ","_"))
os.makedirs(os.path.dirname('hem/'),exist_ok=True)
with open('hem/DIlWed_Aug_17_15_25_05_2022.txt','a') as file:
    file.write("Hello")