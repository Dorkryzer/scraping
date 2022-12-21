from tkinter import *
from tkinter import ttk

def onClick(i,j):
    print("This is Button: "+ str(i) +"/"+str(j))
    

def start():
    #create root and button list
    buttons = []
    win = Tk()
    win.title('dota buff compare')
    win.config(bg='#5F734C')
    win.geometry("1000x600")

    #create frame
    frame = Frame(win,bg='#A8B9BF')
    frame.pack(fill=BOTH,expand=1)

    #create frame
    my_canvas = Canvas(frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #create scrollbar  
    sb = ttk.Scrollbar(frame,orient=VERTICAL,command=my_canvas.yview)
    sb.pack(side=RIGHT,fill=Y)
    
    #configure canvas
    my_canvas.configure(yscrollcommand=sb.set)
    my_canvas.bind('<Configure>',lambda event:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    
    #second frame
    frame2 = Frame(my_canvas)
    my_canvas.create_window((0,0),window=frame2,anchor="nw")

    label = Label(frame2,text="enter player name")
    label.grid(row=0, column=0)

    #create buttons
    for i in range(1,11):
        for j in range(1,21):
            b = Button(frame2, height=2, width=5,text='%s/%s'%(i,j), command=lambda i=i,j=j: onClick(i,j)).grid(row=i,column=j,padx=2,pady=2)
            buttons.append(b)
    win.mainloop()
start()

