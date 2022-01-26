import os
# app fuction will convert the file to executable file
def app():
 s=input("Have you installed python-pyinstaller(y/n)? ")
 if s=='y':
  try:
   import os
   os.system("pyinstaller -i images.ico -F google.py")
   a=os.getcwd()
   b=a+'/dist/google.exe'
   o=input("you are using terminal or cmd(t/c)? ")
   if o=='t':
       os.system(f"cp {b} {a}")
       os.system("rm -r build")
       os.system("rm -r dist")
       os.system("rm google.spec")
       os.system("rm -r __pycache__")
       os.system("rm .gi*")
       os.system("rm *.py")
       os.system("rm image*")
       os.system("rm LICENSE")
       os.system("rm README.md")
   elif o=='c':
               os.system(f"copy {b} {a}")
               os.system("rmdir /s build") 
               os.system("rmdir /s dist")
               os.system("del google.spec")
               os.system("rmdir /s __pycache__")
               os.system("del gi*")
               os.system("del *.py")
               os.system("del image*")
               os.system("del LICENSE")
               os.system("del README.md")
  except :
        print("an error occured, try agaian!!")
 else:
        print("kindly install python-pyinstaller")
        m=input("can i install it(y/n)? ")
        if m=='y':
                  try:
                        os.system("pip install pyinstaller")
                        app()
                  except:
                        print("operation stopped,an error occured")      


if __name__=="__main__":
        
          app()                

