from Tkinter import *

import ttk
import tkMessageBox
from gtts import gTTS
import os
import googletrans
from googletrans import Translator
import speech_recognition as sr


r = sr.Recognizer()


		
translator = Translator()

frm=Tk()

fnt='None 30 bold'
bg='#2eAfB1'
bgtxt='#f35FaA'
fg='#a000f0'
fw=700
fh=500
x=(frm.winfo_screenwidth()-fw)/2 -200
y=(frm.winfo_screenheight()-fh)/2 -50
pad=10
frm.geometry("%dx%d+%d+%d"%(fw,fh,x,y))
frm.title('Employee File Data')
frm.config(bg=bg)

Label(frm,text='Translate English sentence ',bg='navy',fg='lightblue',font=fnt).pack(pady=pad)

frame=Frame(frm,bg=bg)
frame.pack(pady=pad)

Label(frame,text='Text :',bg=bg,fg=fg,font=fnt).grid(row=0,column=0)
Label(frame,text='Speak :',bg=bg,fg=fg,font=fnt).grid(row=1,column=0)
Label(frame,text='Result',bg=bg,fg=fg,font=fnt).grid(row=2,column=0)

svcode=StringVar()
svname=StringVar()


txtcode=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svcode)
txtname=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svname)


cbx1=ttk.Combobox(frame,values=('Arabic','Frensh','german'),state='readonly')
cbx1.current(0)#bache itkta fiha case 0
cbx1.grid(row=3,column=0,pady=pad)
def listen():
        
        
	with sr.Microphone() as source :
		print('Speak Anything : ')
		tkMessageBox.showinfo("Title", "Speak Anything :")
		audio = r.listen(source)
	 
		try:
			txt = r.recognize_google(audio)
			print('You said : {}'.format(txt))
			txt=translator.translate(txt , dest='fr').text
                        
			tts= gTTS(txt ,lang='fr')#lang='ar'
			tts.save('hello.mp3')
			os.system('hello.mp3')
		except:
			print('Sorry could not recognize your voice')

txtcode.grid(row=0,column=1,pady=pad)
ttk.Button(frame,text='Speak Now',command=listen).grid(row=1,column=1)
txtname.grid(row=2,column=1,pady=pad)





def create():

    if cbx1.get()=='Arabic':
        langue='ar'
    elif  cbx1.get()=='Frensh':
        langue='fr'
    else : langue='de'

    
    
    txt=translator.translate(svcode.get() , dest=langue).text
    svname.set(txt)
    tts= gTTS(txt ,lang=langue)#lang='ar'
    tts.save('hello.mp3')
    os.system('hello.mp3')

btnstyle=ttk.Style()
btnstyle.configure('TButton',font=fnt,pady=pad,padding=pad)
ttk.Button(frm,text='Translate',command=create).pack(pady=pad)#mili kin ttk Style aydar direct 
ttk.Button(frm,text='Exit Now',command=frm.destroy).pack(pady=pad)

frm.mainloop()
input("Press enter to exist...")

