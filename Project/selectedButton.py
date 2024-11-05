from tkinter import *
from PIL import Image,ImageTk

class SelectedButton(Button):

   def __init__(self, master, text):
      self.__font = 'Helvetica 10 bold'
      self.__unselected_image = ImageTk.PhotoImage(((Image.open('icons/emptyCircle.PNG')).resize((20, 20))))
      self.__selected_image = ImageTk.PhotoImage(((Image.open('icons/fillCircle.PNG')).resize((20, 20))))
      super(SelectedButton, self).__init__(master, text=" "+text, font=self.__font,\
                                         image=self.__unselected_image, compound= LEFT, highlightthickness = 0, bd = 0, relief=SUNKEN)

   def set_selected_image(self):
      self.config(image=self.__selected_image)

   def set_unselected_image(self):
      self.config(image=self.__unselected_image)
