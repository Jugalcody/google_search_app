import os
# app fuction will convert the file to executable file
def app():
 s=input("Have you installed python-pyinstaller(y/n)? ")
 if s=='y':
  try:
   os.system("pyinstaller -i image.ico -F google.py")
   a=os.getcwd()
   b=a+'/dist/google.exe'
   os.system(f"cp {b} {a}")
   os.system("rm -r build")
   os.system("rm -r dist")
   os.system("rm google.spec")
   os.system("rm -r __pycache__")
   os.system("rm gi*")
   os.system("rm *.py")
   os.system("rm image*")
   os.system("rm LICENSE")
   os.system("rm README.md")
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

