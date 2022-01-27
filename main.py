import os
# app fuction will convert the file to executable file
def app():
 s=input("have you installed python-pyinstaller(y/n)? ")
 if s=='y':
   try:
     import os
     os.system("pyinstaller -i images.ico -F google.py")
   except :
        print("an error occured, try agaian!!")
        os.system(f"pip install https://github.com/pyinstaller/pyinstaller/tarball/develop ")
        app()
   a=os.getcwd()
   b=a+'/dist/google'
   c=a+'\dist\google.exe'
   o=input("you are using terminal or cmd(t/c)? ")
   if o=='t':
       os.system(f"cp {b} {a}")
       os.system("rm -r build")
       os.system("rm -r dist")
       os.system("rm google.spec")
       os.system("rm -r __pycache__")
       os.system("rm -r .gitignore")
       os.system("rm main.py")
       os.system("rm google.py")
       os.system("rm images.ico")
       os.system("rm LICENSE")
       os.system("rm README.md")
       os.system("rm run2.py")
       os.system("chmod +x google")
       os.system("chmod +x run.py")
       f=open(".zshrc","a+")
       v=os.getcwd()
       f.write(f"export PATH=$PATH:{v}")
       os.system("source ~/.zshrc")
       f.close()
       os.system("sudo cp google /bin")
       os.system("sudo cp run.py /bin")
   elif o=='c':
               os.system(f"copy {c} {a}")
               print("Enter y ----\n")
               os.system("rmdir /s build")
               print("Enter y ----\n")
               os.system("rmdir /s dist")
               os.system("del google.spec")
               print("Enter y ----\n")
               os.system("rmdir /s __pycache__")
               os.system("del *git*")
               os.system("del main.py")
               os.system("del google.py")
               os.system("del images.ico")
               os.system("del LICENSE")
               os.system("del README.md")
               os.system("del run.py")
             
 else:
               import os                   
               os.system(f"pip install https://github.com/pyinstaller/pyinstaller/tarball/develop ")
               app()
                        
                                     
if __name__=="__main__":
          import os
          app()
          if(os.path.isfile('run.py')):
                 os.system('python3 run.py')
          elif(os.path.isfile('run2.py')):
                 os.system('python run2.py')
                        
                 
          
                          

