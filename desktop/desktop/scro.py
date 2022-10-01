from tkinter import *
root=Tk()
frame=Frame(root,width=300,height=300)
frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))

hbar=Scrollbar(frame,orient=HORIZONTAL)

hbar.grid(row=1, column=1,fill=X)

hbar.config(command=canvas.xview)

vbar=Scrollbar(frame,orient=VERTICAL)

#vbar.grid(row=1, column=1,fill=Y)
vbar.config(command=canvas.yview)

[Label(frame, text="hello").pack() for i in range(200)]

canvas.config(width=300,height=300)
canvas.config(yscrollcommand=vbar.set)

canvas.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()
