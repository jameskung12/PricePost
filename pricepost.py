"""Parcel function available, w/o debug for floats"""
from Tkinter import *
def w_exit():
    import sys; sys.exit()
def parcel(fees=20):
    """
    input : weight of your parcel (in kgs)
    output : fees of parcel sending
    limitation is 20kgs
    """
    print "Please enter weight of parcel"
    weight = input()
    for i in range(1, weight):
        fees += 15
    print "Total fees is:", fees, "BHT"
root = Tk()
root.title("PricePost (Prototype)")
top_label = Label(root, text="Welcome to PricePost")
btn_post = Button(root, text="Click here for postal")
btn_parcel = Button(root, text="Click here for parcel", command=parcel)
btn_trans = Button(root, text="Click here for money transfer")
btn_exit = Button(root, text="Exit", command=w_exit)
top_label.pack()
btn_post.pack()
btn_parcel.pack()
btn_trans.pack()
btn_exit.pack()
root.mainloop()
