#from PIL import Image, ImageTK
import Tkinter
from Tkinter import *
from ttk import Frame, Style, Button
from productgroup import ProductGroup

class Testgui(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Zappos Test")
		# self.pack(fill=BOTH, expand=1)
		self.style = Style()
		# self.style.theme_use("default")
		# Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
		self.style.configure("My.TFrame", background="red")
		self.prodbox = Listbox(self)
		self.prodbox.bind("<<ListboxSelect>>", self.displayInfo)
		# prods = []
		self.columnconfigure(0, pad=3,weight=1)
		self.columnconfigure(1, pad=3,weight=1,minsize=100)
		self.columnconfigure(2, pad=3,weight=1)
		self.columnconfigure(3, pad=3,weight=1,minsize=100)
		self.columnconfigure(4, pad=3)

		self.rowconfigure(1,weight=1)

		self.currentName = StringVar()
		self.currentPrice = StringVar()

		self.dataFrame = Frame(self,style='My.TFrame')
		self.dataFrame.grid(row=1,column=1,columnspan=3, rowspan=1,sticky=E+S+N+W)
		self.dataFrame.config()

		self.nameLabel = Label(self.dataFrame, text=0, textvariable=self.currentName, font=('Calibri',20,'bold'))
		self.nameLabel.pack(fill=BOTH,anchor=N,expand=YES)

		self.priceLabel = Label(self.dataFrame, text=0, textvariable=self.currentPrice,font=('Calibri',20,'bold'))
		self.priceLabel.pack(fill=BOTH,anchor=N,expand=YES)

		self.price_entry = Scale(self,from_=10, to=1000,orient=HORIZONTAL,bg="gray",resolution=5)
		self.num_entry = Scale(self,from_=1,to=10,orient=HORIZONTAL,bg="gray")

		Label(self, text="Target price",bg="gray").grid(row=0,column=0,sticky=E+N+S+W)
		self.price_entry.grid(row=0, column=1,sticky=W+E)
		Label(self, text="Number of items",bg="gray").grid(row=0,column=2,sticky=E+N+S+W)
		self.num_entry.grid(row=0, column=3,sticky=W+E)

		goButton = Button(self, text="Go!",command=self.refresh)
		goButton.grid(row=0,column=4,sticky=N+E)

		# frame = Frame(self, relief=RAISED, borderwidth=1)
		# frame.grid
		self.prodbox.grid(row=1,column=0,rowspan=2, sticky=S+W+N+E)

		# for p in prods:
			# self.prodbox.insert(END, p)

		self.pack(fill=BOTH,expand=1)

	def refresh(self):
		self.prodbox.delete(0,END)
		self.items = ProductGroup(self.num_entry.get(),self.price_entry.get())
		successful = self.items.populateAll()
		while not successful:
			successful = self.items.populateAll()
		pNames = self.items.returnAllByKey("productName")
		for p in pNames:
			self.prodbox.insert(END, p)

	def displayInfo(self,val):
		sender = val.widget
		idx = sender.curselection()
		value = sender.get(idx)
		self.currentPrice.set(self.items.returnOneByProductName(value,'price'))
		self.currentName.set(value)



def main():
	root = Tk()
	# root.geometry("600x500")# +300+300")
	app=Testgui(root)
	root.configure(background='white')
	root.mainloop()

if __name__ == "__main__":
	main()