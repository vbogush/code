from tkinter import *
tk=Tk()
tk.geometry ("200x320")
tk.title("Calculator")
ent = Entry(justify="right",font="14")
ent.place(x=20,y=20,width=160,height=30)

a=0
b=None


def BC_click():
    ent.delete(0,END)
BC=Button(text="C",font="14",command=BC_click)
BC.place(x=20,y=70,width=80,height=40)

def Equal_click():
    global a,b
    c=float(ent.get())
    if b=="+":
        a=a+c
    if b=="-":
        a=a-c
    if b=="*":
        a=a*c
    if b=="/":
        a=a/c
    ent.delete(0,END)
    ent.insert(END,a)
Equal=Button(text="=",font="14",command=Equal_click)
Equal.place(x=100,y=70,width=80,height=40)

def B0_click():
    ent.insert(END,"0")
B0=Button(text="0",font="14",command=B0_click)
B0.place(x=20,y=250,width=80,height=40)

def Point_click():
    ent.insert(END,".")
Point=Button(text=".",font="14",command=Point_click)
Point.place(x=100,y=250,width=40,height=40)

def Plus_click():
    global a,b
    a=float(ent.get())
    b="+"
    ent.delete(0,END)
Plus=Button(text="+",font="14",command=Plus_click)
Plus.place(x=140,y=250,width=40,height=40)




def B1_click():
    ent.insert(END,"1")
B1=Button(text="1",font="14",command=B1_click)
B1.place(x=20,y=210,width=40,height=40)

def B2_click():
    ent.insert(END,"2")
B2=Button(text="2",font="14",command=B2_click)
B2.place(x=60,y=210,width=40,height=40)

def B3_click():
    ent.insert(END,"3")
B3=Button(text="3",font="14",command=B3_click)
B3.place(x=100,y=210,width=40,height=40)


def Minus_click():
    global a,b
    a=float(ent.get())
    b="-"
    ent.delete(0,END)
Minus=Button(text="-",font="14",command=Minus_click)
Minus.place(x=140,y=210,width=40,height=40)




def B4_click():
    ent.insert(END,"4")
B4=Button(text="4",font="14",command=B4_click)
B4.place(x=20,y=170,width=40,height=40)

def B5_click():
    ent.insert(END,"5")
B5=Button(text="5",font="14",command=B5_click)
B5.place(x=60,y=170,width=40,height=40)

def B6_click():
    ent.insert(END,"6")
B6=Button(text="6",font="14",command=B6_click)
B6.place(x=100,y=170,width=40,height=40)

def Multiply_click():
    global a,b 
    a=float(ent.get())
    b="*"
    ent.delete(0,END)
Multiply=Button(text="*",font="14",command=Multiply_click)
Multiply.place(x=140,y=170,width=40,height=40)



def B7_click():
    ent.insert(END,"7")
B7=Button(text="7",font="14",command=B7_click)
B7.place(x=20,y=130,width=40,height=40)

def B8_click():
    ent.insert(END,"8")
B8=Button(text="8",font="14",command=B8_click)
B8.place(x=60,y=130,width=40,height=40)

def B9_click():
    ent.insert(END,"9")
B9=Button(text="9",font="14",command=B9_click)
B9.place(x=100,y=130,width=40,height=40)


def Divide_click():
    global a,b 
    a=float(ent.get())
    b="/"
    ent.delete(0,END)
Divide=Button(text="/",font="14",command=Divide_click)
Divide.place(x=140,y=130,width=40,height=40)

tk.mainloop()
