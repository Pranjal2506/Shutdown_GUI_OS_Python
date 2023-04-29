import os
from tkinter import *
t=255

def restart():
    os.system("shutdown /r /t 1")
    st.destroy()

def logout():
    os.system("shutdown -1")
    st.destroy()
    
def shutdown():
    os.system("shutdown /s /t 1")
    st.destroy()
def time():
    global textfield
    global temp
    temp=Toplevel(st)
    temp.geometry("400x200")
    temp.config(bg="lightblue")
    label=Label(temp,text="Enter time in seconds",font=("Ariel",12,"bold italic underline"),bg="lightblue")
    label.pack(side=TOP)
    textfield=Entry(temp,font=("Ariel",10,"bold italic"))
    textfield.place(x=125,y=100,height=50,width=150)
    btn=Button(temp,text="Confirm!",command=shut)
    btn.place(x=125,y=175)
    btn2=Button(temp,text="Close",command=close_temp)
    btn2.place(x=235,y=175)

def close_temp():
    temp.destroy()
def shut():
    time=textfield.get()
    os.system(f"shutdown /s /t {time}")
    st.destroy()


st= Tk()
st.title("Shutdown")
st.geometry("500x500")
st.config(bg="lightblue")

button1=Button(st,text="Restart",font=("Comic Sans Ms", 18, "bold"),relief=RAISED,command=restart)
button1.place(x=175,y=10,height=50,width=150)

button2=Button(st,text="Shutdown-Time",font=("Comic Sans Ms",15,"bold"),relief=RAISED,command=time)
button2.place(x=175,y=70,height=50,width=150)

button3=Button(st,text="Shutdown",font=("Comic Sans Ms",18,"bold"),relief=RAISED,command=shutdown)
button3.place(x=175,y=130,height=50,width=150)

button3=Button(st,text="logout",font=("Comic Sans Ms",18,"bold"),relief=RAISED,command=logout)
button3.place(x=175,y=190,height=50,width=150)


    
st.mainloop()
