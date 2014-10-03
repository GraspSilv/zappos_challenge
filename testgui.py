# from PIL import Image, ImageTK
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
		# style.configure("Frame", background="#333")
		prodbox = Listbox(self)
		prods = []
		self.columnconfigure(0, pad=3,weight=1)
		self.columnconfigure(1, pad=3,weight=1,minsize=100)
		self.columnconfigure(2, pad=3,weight=1)
		self.columnconfigure(3, pad=3,weight=1,minsize=100)
		self.columnconfigure(4, pad=3)

		self.rowconfigure(1,weight=1)

		price_entry = Scale(self,from_=10, to=1000,orient=HORIZONTAL)
		num_entry = Scale(self,from_=1,to=10,orient=HORIZONTAL)

		Label(self, text="Target price").grid(row=0,column=0,sticky=E+N+S+W)
		price_entry.grid(row=0, column=1,sticky=W+E)
		Label(self, text="Number of items").grid(row=0,column=2,sticky=E+N+S+W)
		num_entry.grid(row=0, column=3,sticky=W+E)

		goButton = Button(self, text="Go!")
		goButton.grid(row=0,column=4,sticky=N+E)

		# frame = Frame(self, relief=RAISED, borderwidth=1)
		# frame.grid
		prodbox.grid(row=1,column=0,rowspan=2, sticky=S+W+N+E)

		for p in prods:
			lb.insert(END, p)

		self.pack(fill=BOTH,expand=1)

def main():
	root = Tk()
	# root.geometry("600x500")# +300+300")
	app=Testgui(root)
	root.configure(background='white')
	root.mainloop()

if __name__ == "__main__":
	main()