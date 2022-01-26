import os
s=input("Have you installed python-pyinstaller(y/n)? ")
if s=='y':
 try:
  os.system("pyinstaller -i image.ico -F google.py")
  a=os.getcwd()
  b=a+'/dist/google.exe'
  n=input("what is your os(ubuntu/linux/windows/Mac-OS) : ")
  n=n.lower()
  if(n=='ubuntu' or n=='linux' or n=='mac-os'):
                os.system(f"cp {b} {a}")
                os.system("rm -r build")
                os.system("rm -r dist")
  elif(n=="windows"):
                os.system(f"copy {b} {a}")                 
                os.system("rmdir /s build")
                os.system("rmdir /s dist")
 except :
             print("an error occured, try agaian!!")
else:
        print("kindly install python-pyinstaller")
        m=input("can i install it(y/n)? ")
        if m=='y':
                  try:
                        os.system("pip install pyinstaller")
                  except:
                        print("operation stopped,an error occured")      
                

