# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import Tk, Frame, BOTH, filedialog, constants

#Example inherits from Frame
class Window(Frame):
    #Constructor method
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        #Save a reference to the parent widget 
        self.parent = parent
        #Delegate the UI's creation to this method
        self.initUI()
        
    
    def initUI(self):
        #Set title of the window to "Simple"
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        buttonOpt = {'fill': constants.X, 'padx': 5, 'pady': 5}
        tkinter.Button(self, text="Open file...",
                                command=self.askopenfile).pack(**buttonOpt)
        self.file_opt = options = {}
        options['defaultextension'] = '.xml'
        options['filetypes'] = [('Results files', '.xml')] 
        options['initialdir'] = 'C:\\'
        options['parent'] = self.parent
        options['title'] = 'Open a file...' 

                      
    def askopenfile(self):
        return tkFileDialog.askopenfile(mode='r', **self.file_opt)
        

def main():
  
    root = Tk()
    #Set the size of the window and its position
    root.geometry("500x400+200+100")
    #Create an instance of the Example class
    app = Window(root)
    root.mainloop()  


if __name__ == '__main__':
    main()