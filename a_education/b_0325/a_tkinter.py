from tkinter import *



root = Tk() #객체 생성


lbl = Label(root, text="성명")
lbl.pack()

txt = Entry(root)
txt.pack()

root.mainloop() #객체호출
