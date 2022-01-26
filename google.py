import tkinter as tk
import webbrowser as wb,re,os
class Google:  #Google class will create a google search engine 
    def __init__(self):
           
           self.root=tk.Tk()
           self.root.title("Google")
           self.root.resizable(False,False)
           self.root.geometry('600x400+350+160')
           l=tk.Label(self.root,text="ALL")
           l.place(relx=0.01,rely=0.01)

           m=tk.Label(self.root,text="IMAGES")
           m.place(relx=0.09,rely=0.01)
           
           email=tk.Label(self.root,text="GMAIL")
           email.place(relx=0.87,rely=0.01)

           g=tk.Label(self.root,text="GOOGLE",font=("Helvatical Bold",30))
           g.place(relx=0.34,rely=0.3)

           t=tk.Entry(self.root)
           t.place(relx=0.24,rely=0.5,width=300,height=35)
           
           
           def search():
                  s=t.get()
                  if(re.fullmatch(r'www.+\b[A-Za-z0-9_-]+.[A-Z|a-z]\b',s)):
                                   wb.open(s)
                  else:                 
                                   wb.open('https://www.google.com/search?q='+s+'&oq=github&aqs=chrome..69i57j46i199i433i465i512j0i433i512j69i59j0i512j69i60l3.4076j0j7&sourceid=chrome&ie=UTF-8')

           b=tk.Button(self.root,text="search",command=search)
           b.place(relx=0.42,rely=0.64)
           
           l.bind("<Button>",lambda e: wb.open("https://www.google.com"))
           
           m.bind("<Button>",lambda e: wb.open("https://www.google.co.in/imghp?hl=en-GB&tab=ri&ogbl"))
           
           email.bind("<Button>",lambda e: wb.open("https://mail.google.com/mail/u/0/"))
           n=f'{os.getcwd()}/image.png'
           a=tk.PhotoImage(file=n)
           self.root.iconphoto("False",a)
           self.root.mainloop()



if __name__=="__main__":

       root=Google()
       

