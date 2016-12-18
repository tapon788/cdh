from Tkinter import *
class Demo(Frame):
    def __init__(self, parent=None, **args):
        Frame.__init__(self, parent, args)
	self.config(bd=5,bg="#ddffdd")
        self.pack()
	self.var=StringVar()
	self.var.set("true")
	r_true=Radiobutton(self,text="True",variable=self.var,value="true")
	r_true.config(relief=SUNKEN,bg="#aaffaa")
	r_true.pack(side=LEFT)
	r_false=Radiobutton(self,text="False",variable=self.var,value="false")
	r_false.config(relief=SUNKEN,bg="#aaffaa")
	r_false.pack(side=RIGHT)

    def t_f(self):
	true_false=self.var.get()
	return true_false




if __name__ == '__main__' :
    Demo().mainloop()
