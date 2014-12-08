"""
Changelog
1) Moving main window function to separate function
2) Adding postal and money function but still not working
3) Adding limitation exceed warning for parcel function
"""
from Tkinter import *
def w_exit():
    """
    window exit function
    """
    import sys; sys.exit()
#def postal(fees_s=3, fees_r=16, fees_e=32):
    #"""
    #input :
    #1)
    #2) weight of your postal (in kg)
    #output : fees of postal sending
    #"""
def parcel(fees=20):
    """
    input : weight of your parcel (in kg)
    output : fees of parcel sending
    limitation is 20kg
    """
    print "Please enter weight of parcel"
    weight = input()
    if weight > 20:
        print "Limitation of sending is 20kg"
    else:
        for i in range(1, int(weight) + 1):
            fees += 15
        print "Total fees is:", fees, "BHT"
#def money(fees_s=10, fees_e=41):
    #"""
    #input :
    #1) type of money sending (standard or EMS)
    #2) numbers of money to sending (in BHT)
    #output : fees of money sending
    #limitation is 50,000BHT
    #"""
def main_prog():
    """
    main program
    """
    root = Tk()
    root.title("PricePost (Prototype)")
    top_label = Label(root, text="Welcome to PricePost")
    btn_post = Button(root, text="Click here for postal")
    btn_parcel = Button(root, text="Click here for parcel", command=parcel)
    btn_trans = Button(root, text="Click here for money transfer")
    btn_about = Button(root, text="About")
    btn_exit = Button(root, text="Exit", command=w_exit)
    top_label.pack()
    btn_post.pack()
    btn_parcel.pack()
    btn_trans.pack()
    btn_about.pack()
    btn_exit.pack()
    root.mainloop()
main_prog()
