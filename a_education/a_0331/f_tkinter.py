# from tkinter import *
# root = Tk()
#
# lbl = Label(root, text='성명')
# lbl.pack()
#
#
# txt = Entry(root)
# txt.pack()
#
#
# btn = Button(root, text='OK')
# btn.pack()
#
# root.mainloop()




# #2
# from tkinter import *
# root = Tk()
#
# lbl = Label(root, text='성명')
# lbl.grid(row=0, column=0)
#
#
# txt = Entry(root)
# txt.grid(row=0, column=1)
#
#
# btn = Button(root, text='OK', width=15)
# btn.grid(row=1, column=1)
#
# root.mainloop()



# #3
# from tkinter import *
# window = Tk()
#
#
#
# w = Label(window, text='색깔변환1',bg='red', fg='white')
# w.place(x=0,y=0)
#
# w = Label(window, text='색깔변환2',bg='green', fg='black')
# w.place(x=20,y=20)
#
#
# window.mainloop()





# #4
# from tkinter import *
#
# def process():
#     print("Hello?")
#
# window = Tk()
#
#
# btn = Button(window, text='클릭', width=15, command=process)
# btn.grid(row=1, column=1)
# window.mainloop()



#4
from tkinter import *
from tkinter import messagebox

# 버튼클릭 이벤트 핸들러
def okClick():
    name = txt.get()

    messagebox.showinfo("이름", name)

root = Tk()
lbl = Label(root,text="이름")
lbl.grid(row=0,column=0)

txt = Entry(root)
txt.grid(row=0,column=1)

#버튼클릭 이벤트와 핸들러 정의

btn = Button(root, text='클릭', width=15, command=okClick)
btn.grid(row=1, column=1)


root.mainloop()





