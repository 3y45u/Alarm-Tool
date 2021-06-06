from tkinter import *
from tkinter import messagebox
import datetime
from playsound import playsound

window = Tk()
window.geometry("300x500")
window.title("ALARM TOOL")
window.config(background="lightgrey")

def ring():
    hour=int(hrs.get())
    minute=int(mints.get())
    c=v.get()
    snooze_time=int(snzt.get())
    alarm_text=alr.get()
    if c==1 and hour!=12:
        hour=hour+12
    while True:
        if(hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute):
            playsound('C:\\Users\\Gagan Raturi\\Desktop\\CLASS\\int213\\project\\program\\Twin-bell-alarm-clock.mp3')
            playsound('C:\\Users\\Gagan Raturi\\Desktop\\CLASS\\int213\\project\\program\\Twin-bell-alarm-clock.mp3')
            new_window=Tk()
            new_window.geometry("300x300")
            new_window.title("Ringing")
            new_window.config(background="lightgrey")
            
            def snz():
                min2=datetime.datetime.now().minute
                min2=min2+snooze_time
                while True:
                    if(min2==datetime.datetime.now().minute):
                        playsound('C:\\Users\\Gagan Raturi\\Desktop\\CLASS\\int213\\project\\program\\Twin-bell-alarm-clock.mp3')
                        playsound('C:\\Users\\Gagan Raturi\\Desktop\\CLASS\\int213\\project\\program\\Twin-bell-alarm-clock.mp3')
                        break
                    
            def ext():
                new_window.destroy()
                
            new_l1=Label(new_window,text=alarm_text,background="lightgrey")
            new_l1.config(font=("Times",24,'bold'))
            new_b1=Button(new_window,text="Snooze",command=snz,background="lightgrey")
            new_b1.config(font=("Times",16,'bold'))
            new_b2=Button(new_window,text="Exit",command=ext,background="lightgrey")
            new_b2.config(font=("Times",16,'bold'))
            new_l1.grid(row=0,column=0,columnspan=2)
            new_b1.grid(row=1,column=0)
            new_b2.grid(row=1,column=1)
            new_window.mainloop()

def settime():
    hour2=int(hrs2.get())
    minute2=int(mints2.get())
    h2=datetime.datetime.now().hour+hour2
    m2=datetime.datetime.now().minute+minute2
    while True:
        if(h2==datetime.datetime.now().hour and m2==datetime.datetime.now().minute):
            playsound('C:\\Users\\Gagan Raturi\\Desktop\\CLASS\\int213\\project\\program\\Twin-bell-alarm-clock.mp3')
            playsound('C:\\Users\\Gagan Raturi\\Desktop\\CLASS\\int213\\project\\program\\Twin-bell-alarm-clock.mp3')
            break
            
    
st=Label(window,text="Set Time :",background="lightgrey")
st.config(font=("Times",24,'bold'))
l1=Label(window,text="Hours :",background="lightgrey")
l1.config(font=("Times",14))
l2=Label(window,text="Minutes :",background="lightgrey")
l2.config(font=("Times",14))

hrs=Spinbox(window,from_=00,to=12,bd=3)
hrs.config(font=("Times",11))
mints=Spinbox(window,from_=00,to=59,bd=3)
mints.config(font=("Times",11))

v=IntVar()
r1=Radiobutton(window,text="A.M.",variable=v,value=0,background="lightgrey")
r1.config(font=("Times",11))
r2=Radiobutton(window,text="P.M.",variable=v,value=1,background="lightgrey")
r2.config(font=("Times",11))

l3=Label(window,text="Snooze Time : ",background="lightgrey")
l3.config(font=("Times",14))
snzt=Spinbox(window,from_=1,to=30,bd=3)
snzt.config(font=("Times",11))

l4=Label(window,text="Alarm Label : ",background="lightgrey")
l4.config(font=("Times",14))
alr=Entry(window,bd=3)
alr.config(font=("Times",11))

b1=Button(window,text="Set Alarm",command=ring,background="lightgrey")
b1.config(font=("Times",16,'bold'))

l5=Label(window,text="Timer:",background="lightgrey")
l5.config(font=("Times",24,'bold'))
l6=Label(window,text="Hours :",background="lightgrey")
l6.config(font=("Times",14))
l7=Label(window,text="Minutes :",background="lightgrey")
l7.config(font=("Times",14))
hrs2=Spinbox(window,from_=00,to=24,bd=3)
hrs2.config(font=("Times",11))
mints2=Spinbox(window,from_=00,to=59,bd=3)
mints2.config(font=("Times",11))
b2=Button(window,text="Set Time",command=settime,background="lightgrey",fg='black')
b3=Button(window,text="Exit",command=exit,background="lightgrey",fg='red')
b2.config(font=("Times",16,'bold'))
b3.config(font=("Times",16,'bold'))

hour=IntVar()
minute=IntVar()
hour2=IntVar()
minute2=IntVar()

st.grid(row=0,column=1,columnspan=3)
l1.grid(row=1,column=2)
l2.grid(row=2,column=2)
hrs.grid(row=1,column=3)
mints.grid(row=2,column=3)
r1.grid(row=3,column=3)
r2.grid(row=4,column=3)
l3.grid(row=6,column=2)
snzt.grid(row=6,column=3)
l4.grid(row=8,column=2)
alr.grid(row=8,column=3)
b1.grid(row=9,column=3)

l5.grid(row=10,column=1,columnspan=3)
l6.grid(row=11,column=2)
l7.grid(row=12,column=2)
hrs2.grid(row=11,column=3)
mints2.grid(row=12,column=3)
b2.grid(row=13,column=2,columnspan=3)
b3.grid(row=14,column=2,columnspan=3)

window.mainloop()
