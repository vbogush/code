from tkinter import *
tk=Tk()
tk.geometry ("440x300")
tk.title("Pizza")

name=Label(text="Naming",font=("Arial",12,"bold"))
name.place(x=20,y=20)


price=Label(text="Price, UAH.",font=("Arial",12,"bold"))
price.place(x=150,y=20)


number=Label(text="Quantaty",font=("Arial",12,"bold"))
number.place(x=230,y=20)


cost=Label(text="Total, UAH",font=("Arial",12,"bold"))
cost.place(x=310,y=20)


lbl1=Label(text="Pizza",font=("Arial",12))
lbl1.place(x=20,y=60)


lbl2=Label(text="Icecream",font=("Arial",12))
lbl2.place(x=20,y=100)


lbl3=Label(text="Tasty",font=("Arial",12))
lbl3.place(x=20,y=140)


lbl4=Label(text="Juce",font=("Arial",12))
lbl4.place(x=20,y=180)

lbl1=Label(text="Pizza",font=("Arial",12))
lbl1.place(x=20,y=60)


p1=Entry(font="Arial 12",bg="sky blue",justify="center")
p1.insert(END,"75")
p1.place(x=150,y=60,width=60,height=30)


p2=Entry(font="Arial 12",bg="sky blue",justify="center")
p2.insert(END,"12")
p2.place(x=150,y=100,width=60,height=30)


p3=Entry(font="Arial 12",bg="sky blue",justify="center")
p3.insert(END,"16")
p3.place(x=150,y=140,width=60,height=30)


p4=Entry(font="Arial 12",bg="sky blue",justify="center")
p4.insert(END,"8")
p4.place(x=150,y=180,width=60,height=30)


y1=0
y2=0
y3=0
y4=0


def rez(y):
    if y==int(y):
        return(int(y))
    else:
        return(y)



def s1_click(val):
    global y1
    k1=int(val)
    x1=float(p1.get())
    y1=x1*k1
    var1.set(rez(y1))

s1=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s1_click)
s1.place(x=230,y=50)



def s2_click(val):
    global y2
    k2=int(val)
    x2=float(p2.get())
    y2=x2*k2
    var2.set(rez(y2))

s2=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s2_click)
s2.place(x=230,y=90)



def s3_click(val):
    global y3
    k3=int(val)
    x3=float(p3.get())
    y3=x3*k3
    var3.set(rez(y3))

s3=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s3_click)
s3.place(x=230,y=130)



def s4_click(val):
    global y4
    k4=int(val)
    x4=float(p4.get())
    y4=x4*k4
    var4.set(rez(y4))

s4=Scale(orient=HORIZONTAL,length=50,from_=0,to=10,command=s4_click)
s4.place(x=230,y=170)



var1=StringVar()
c1=Label(text=0,font="Arial 12",bg="deep sky blue",textvariable=var1)
c1.place(x=310,y=60,width=60,height=30)

var2=StringVar()
c2=Label(text=0,font="Arial 12",bg="deep sky blue",textvariable=var2)
c2.place(x=310,y=100,width=60,height=30)

var3=StringVar()
c3=Label(text=0,font="Arial 12",bg="deep sky blue",textvariable=var3)
c3.place(x=310,y=140,width=60,height=30)

var4=StringVar()
c4=Label(text=0,font="Arial 12",bg="deep sky blue",textvariable=var4)
c4.place(x=310,y=180,width=60,height=30)



lbl5=Label(text="Total",font=("Arial",12))
lbl5.place(x=20,y=240)

var5=StringVar()
c5=Label(text=0,font="Arial 12",bg="deep sky blue",textvariable=var5)
c5.place(x=200,y=240,width=60,height=30)


lbl6=Label(text="UAH",font=("Arial",12))
lbl6.place(x=270,y=240)


def btn_click():
    global y1,y2,y3,y4
    y=y1+y2+y3+y4
    var5.set(rez(y))


btn=Button(text="Calculate",font=("Arial",12),command=btn_click)
btn.place(x=310,y=240,height=30)

tk.mainloop()