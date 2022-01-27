#!/usr/bin/python3
import os
if(os.path.isfile('google')):
          os.system("chmod +x google")
          os.system("./google")
elif(os.path.isfile('main.py')):
          os.system('python3 main.py')
          
