from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
import textblob

root=Tk()
root.title('Google tarjimon dasturi')
root.geometry("1080x400")
root.config(bg='white')
root.resizable(False,False)
def label_change():
    c=combo1.get()
    c2=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c2)
    root.after(1000,label_change)

def translate_now():
   try:
       text_ = txt1.get(1.0, END)
       t1 = Translator()
       trans_txt = t1.translate(text_, src=combo1.get(), dest=combo2.get())
       trans_txt = trans_txt.text

       txt2.delete(1.0, END)
       txt2.insert(END, trans_txt)
   except Exception as e:
       messagebox.showerror("googletrans", "iltimos qaytadan urinib ko'ring")


#img

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font='Roboto 14',state='r')
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",
             width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

fram1=Frame(root,bg="Black",bd=5)
fram1.place(x=10,y=118,width=440,height=210)

txt1=Text(fram1,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
txt1.place(x=0,y=0,width=430,height=200)

scroll1=Scrollbar(fram1)
scroll1.pack(side="right",fill="y")
scroll1.configure(command=txt1.yview)
txt1.configure(yscrollcommand=scroll1.set)
combo2=ttk.Combobox(root,values=languageV,font='Roboto 14',state='r')
combo2.place(x=730,y=20)
combo2.set("TILNI TANLANG")

label2=Label(root,text="TILNI TANLANG",font="segoe 30 bold",bg="white",
             width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

fram2=Frame(root,bg="Black",bd=5)
fram2.place(x=620,y=118,width=440,height=210)

txt2=Text(fram2,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
txt2.place(x=0,y=0,width=430,height=200)

scroll2=Scrollbar(fram2)
scroll2.pack(side="right",fill="y")
scroll2.configure(command=txt2.yview)
txt2.configure(yscrollcommand=scroll2.set)

translate=Button(root,text="Tarjima", font="Roboto 20 bold",
                activebackground="purple", cursor="hand2", bd=5,
                bg='red', fg="white",command=translate_now).place(x=470,y=200)
label_change()
root.mainloop()

















