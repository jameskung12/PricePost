"""Added button, but still no on click function"""
from Tkinter import *
root = Tk()
root.title("PricePost (Prototype)")
top_label = Label(root, text="Welcome to PricePost")
top_label.pack()
btn_post = Button(root, text="Click here for postal")
btn_parcel = Button(root, text="Click here for parcel")
btn_trans = Button(root, text="Click here for money transfer")
btn_post.pack()
btn_parcel.pack()
btn_trans.pack()
root.mainloop()
