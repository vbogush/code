from tkinter import *
tk=Tk()
tk.geometry ("260x370")
tk.title("Calculator")
ent = Entry(justify="right",font="14")
ent.place(x=20,y=20,width=220,height=30)
BC=Button(text="C",font="14")
BC.place(x=20,y=70,width=100,height=40)
Equal=Button(text="-",font="14")
Equal.place(x=140,y=70,width=100,height=40)


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

tk.mainloop()
