from Tkinter import *
class Demo(Frame):
    def __init__(self, parent=None, **args):
        Frame.__init__(self, parent, args)
        self.config()
	self.pack()
        #Label(self, text="Cellbarr-DLPC-Hopping").pack()
        self.vars = []
	self.title = ["Cellbarr","DLPC","Hopping"]
        for title in self.title:
            var = IntVar( )
            x=Checkbutton(self,
                        text=title,
                        variable=var)
	    x.config(bg="#fdddaf",font=("verdena",12,'bold'))
	    x.pack(side=LEFT,anchor=NW)
            self.vars.append(var)
	#self.tools()

    def c_d_h(self):
	cdh_var=[]
	for var in self.vars:
            cdh_var.append(var.get( ))
	return cdh_var
  

    #def tools(self):
     #   frm = Frame(self)
      #  frm.pack(side=RIGHT)
       # Button(frm, text='State', command=self.report).pack(fill=X)
        
if __name__=='__main__':
    Demo().mainloop()
