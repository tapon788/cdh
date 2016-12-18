from Tkinter import *
class Demo(Frame):
    def __init__(self, parent=None, **args):
        Frame.__init__(self, parent, args)
	self.pack()
	self.x=Text(self,font=("Verdena",12,'bold'))
	self.x.config(height=15,width=8,bg="#555577",fg="#ffffff")
	self.x.pack(expand=YES,fill=BOTH)
if __name__=='__main__':
    Demo().mainloop()
