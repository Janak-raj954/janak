from tkinter import  *
win=Tk()
win.config(bg='black')
win.geometry('370x465')
x=StringVar()
win.title('Calculator')

def cancell():
    global g
    g=''
    x.set(g)
def delete():
    global g
    g=g[0:-1]
    x.set(g)
def button(num):
    global g
    g=g+str(num)
    x.set(g)
def calulation():
    global g
    try:
        f=(eval(g))
        x.set(f)
        g=''
    except SyntaxError:
        x.set('Error')
        g=''

    except ZeroDivisionError:
        x.set('Error')
        g=''
g=''
result=Label(win,bg='silver',height=2,width=19,fg='black',textvariable=x,font=('Console',25))
result.pack()
frame=Frame(win)

frame.pack()


button_1=Button(frame,text=1,width=10,height=4,bg='#D4D4D2',activebackground='#D4D4D2',font=('console',10),command=lambda :button(1))
button_2=Button(frame,text=2,width=10,height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('2'))
button_3=Button(frame,text=3,width=10,height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('3'))
button_4=Button(frame,text=4,width=10,height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('4'))
button_5=Button(frame,text=5,width=10,height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('5'))
button_6=Button(frame,text=6,width=10,height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('6'))
button_7=Button(frame,text=7,width=10,height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('7'))
button_8=Button(frame,text=8,width=10,height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('8'))
button_9=Button(frame,text=9, width=10, height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('9'))
button_0=Button(frame,text=0,width=10,height=4,font=('console',10),command=lambda :button('0'),activebackground='#D4D4D2',bg='#D4D4D2',)
button_percent=Button(frame,text='=',width=10,height=4,bg='#FF9500',activebackground='#FF9500',font=('console',10),command=calulation)
button_point=Button(frame,text='.',width=10,height=4,font=('console',10),bg='#D4D4D2',activebackground='#D4D4D2',command=lambda :button('.'))
button_multiply=Button(frame,text='×',width=10,height=4,bg='#FF9500',font=('console',10),activebackground='#FF9500',command=lambda :button('*'))
button_addition=Button(frame,text='+',bg='#FF9500',width=10,height=4,font=('console',10),activebackground='#FF9500',command=lambda :button('+'))
button_substraction=Button(frame,text='_',bg='#FF9500',activebackground='#FF9500',width=10,height=4,font=('console',10),command=lambda :button('-'))
button_divide=Button(frame,text='÷',height=4,bg='#FF9500',activebackground='#FF9500',width=10,font=('console',10),command=lambda :button('/'))
button_cancell=Button(frame,text='C',bg='#505050',activebackground='#505050',width=10,height=4,font=('console',10),command=cancell)
button_delete=Button(frame,text='Del',bg='#505050',width=10,activebackground='#505050',height=4,font=('console',10),command=delete)
button_00=Button(frame,text='00',bg='#505050',activebackground='#505050',width=10,height=4,font=('console',10),command=lambda :button('00'))
button_squ=Button(frame,text='Squ',bg='#FF9500',width=10,activebackground='#FF9500',height=4,font=('console',10),command=lambda :button('**'))
button_9.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_7.grid(row=1,column=2)
button_6.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=2)
button_3.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=2)
button_0.grid(row=4,column=1)
button_percent.grid(row=4,column=2)
button_point.grid(row=4,column=0)
button_addition.grid(row=1,column=3)
button_multiply.grid(row=3,column=3)
button_substraction.grid(row=2,column=3)
button_divide.grid(row=4,column=3)
button_cancell.grid(row=0,column=0)
button_delete.grid(row=0,column=1)
button_00.grid(row=0,column=2)
button_squ.grid(row=0,column=3)
win.mainloop()
