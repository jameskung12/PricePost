"""Added on click function on Exit button"""
from Tkinter import *
def w_exit():
    import sys; sys.exit()
root = Tk()
root.title("PricePost (Prototype)")
top_label = Label(root, text="Welcome to PricePost")
btn_post = Button(root, text="Click here for postal")
btn_parcel = Button(root, text="Click here for parcel")
btn_trans = Button(root, text="Click here for money transfer")
btn_exit = Button(root, text="Exit", command=w_exit)
top_label.pack()
btn_post.pack()
btn_parcel.pack()
btn_trans.pack()
btn_exit.pack()
root.mainloop()
