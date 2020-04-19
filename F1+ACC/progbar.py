# importing tkinter module
from tkinter import *
from tkinter.ttk import *


class MojOver:
    def __init__(self):
        # creating tkinter window
        self.root = Tk()
        self.data = 20
        # Progress bar widget
        self.progress = Progressbar(self.root, orient=VERTICAL, length=100, mode='determinate')
        self.progress['value'] = self.data
        self.root.update_idletasks()
        self.progress.pack(pady=1)

        self.root.image = PhotoImage(file='2.png')
        self.label = Label(self.root, image=self.root.image, background='WHITE')
        self.root.overrideredirect(True)
        self.root.geometry("+250+250")
        self.root.lift()
        #self.root.wm_attributes("-topmost", True)
        #self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "white")
        self.label.pack()
        self.label.mainloop()



        self.root.mainloop()

    # Function responsible for the updation
    # of the progress bar value
#def bar(self):
#	print(self.data)


# This button will initialize
# the progress bar
        self.Button(self.root, text='Start').pack(pady=10)
# infinite loop
if __name__ == '__main__':
	obiekt = MojOver()

