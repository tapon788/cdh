from Tkinter import *
class Demo(Frame):
    def __init__(self, parent=None, **args):
        Frame.__init__(self, parent, args)
        self.pack()
	Label(self,text="Site_id",font=("arial",12)).pack(side=LEFT)
	self.site_id=Entry(self,font=("verdena",12,'bold'))
	self.site_id.config(bd=5,bg="#99dddd")
	self.site_id.pack(side=LEFT)
	Label(self,text="Cell_no",font=("arial",12)).pack(side=LEFT)
	self.cell_no=Entry(self,font=("verdena",12,'bold'))
	self.cell_no.config(bd=5,bg="#99dddd")
	self.cell_no.pack(side=LEFT)

    def si(self):
	return self.site_id.get()
    def cn(self):
	return self.cell_no.get()
if __name__ == '__main__' :
    Demo().mainloop()
