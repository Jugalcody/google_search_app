import tkinter as tk
import webbrowser as wb,re,os
class Google:  #Google class will create a google search engine 
    def __init__(self):
           
           self.root=tk.Tk()
           self.root.title("Google")
           self.root.resizable(False,False)
           self.root.geometry('1199x600+70+70')
           l=tk.Label(self.root,text="ALL",cursor="hand2")
           l.place(relx=0.01,rely=0.01)

           m=tk.Label(self.root,text="IMAGES",cursor="hand2")
           m.place(relx=0.055,rely=0.01)
           
           email=tk.Label(self.root,text="GMAIL",cursor="hand2")
           email.place(relx=0.92,rely=0.01)

           g=tk.Label(self.root,text="GOOGLE",font=("Helvatical bold",38))
           g.place(relx=0.4,rely=0.3)
           t=tk.Entry(self.root,font=("Default",14))
           t.place(relx=0.325,rely=0.45,width=400,height=42)
           
           
           def search():
               s=t.get()
               if(s!=''):
                  if(re.match(r'[a-z://a-z.]+\b[A-Za-z0-9_-]+.[A-Z|a-z]\b',s)):
                                   wb.open(s)
                  else:                 
                                   wb.open('https://www.google.com/search?q='+s+'&oq=github&aqs=chrome..69i57j46i199i433i465i512j0i433i512j69i59j0i512j69i60l3.4076j0j7&sourceid=chrome&ie=UTF-8')

           b=tk.Button(self.root,text="search",command=search,cursor="hand2",width=9,height=1)
           b.place(relx=0.45,rely=0.56)
           
           l.bind("<Button>",lambda e: wb.open("https://www.google.com"))
           
           m.bind("<Button>",lambda e: wb.open("https://www.google.co.in/imghp?hl=en-GB&tab=ri&ogbl"))
           
           email.bind("<Button>",lambda e: wb.open("https://mail.google.com/mail/u/0/"))
           
           n=f'{os.getcwd()}/images.png'
           #a=tk.PhotoImage(file=n)
           #self.root.iconphoto("False",a)
           try:
              photo=tk.PhotoImage(file=(r''+str(n)))
              self.root.iconphoto(False,photo)
              
           except:
                 pass
                
           self.root.mainloop()   



if __name__=="__main__":

       root=Google()
       

