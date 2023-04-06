from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + " Mbps"
    up = str(round(sp.upload()/(10**6),3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet speed test")
sp.geometry("500x700")
sp.config(bg="orange")

lab = Label(sp,text = "Internet speed", font= ("Time New Roman",20,"bold"),bg="blue",fg="white")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp,text = "Download speed", font= ("Time New Roman",20,"bold"),bg="white",fg="red")
lab.place(x=60,y=130,height=50,width=380)

lab_down = Label(sp,text = "00", font= ("Time New Roman",20,"bold"),bg="white",fg="red")
lab_down.place(x=60,y=200,height=50,width=380)

lab = Label(sp,text = "Upload speed", font= ("Time New Roman",20,"bold"),bg="white",fg="red")
lab.place(x=60,y=290,height=30,width=380)

lab_up = Label(sp,text = "00", font= ("Time New Roman",20,"bold"),bg="white",fg="red")
lab_up.place(x=60,y=360,height=30,width=380)

button = Button(sp, text = "CHECK SPEED",font= ("Time New Roman",20,"bold"),relief=RAISED,bg="pink",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()
# from tkinter import *

# win = Tk()

# def btn1():
#   print("I Don't Know Your Name")

# button1 =  Button(win, text="Click Me To Print SomeThing", command=btn1)

# button1.pack()
# win.mainloop()