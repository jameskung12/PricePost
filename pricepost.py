"""
Changelog
1) Alpha edition of parcel window
2) Reduced number of line
"""
from Tkinter import *
def w_exit():
    """
    window exit function
    """
    import sys; sys.exit()
#def postal(fees=0):
#def postal_win():
def parcel_win():
    parcel = Tk(); parcel.title("Parcel")
    label1 = Label(parcel, text="Please enter weight (in kg)")
    w_entry = Entry(parcel)
    button1 = Button(parcel, text="Enter")
    label1.pack(); w_entry.pack(); button1.pack()
    parcel.mainloop()
#def money_win():
def parcel(fees=20):
    """
    input : weight of your parcel (in kg)
    output : fees of parcel sending
    limitation is 20kg
    """
    weight = input()
    if weight > 20:
        print "Limitation of sending is 20kg"
    else:
        if weight % 1 == 0:
            weight == int(weight)
        else:
            weight == int(weight) + 1
        for i in range(1, int(weight) + 1):
            fees += 15
        print "Total fees is:", fees, "BHT"
def money(fees=0):
    """
    input :
    1) type of money sending (standard or EMS)
    2) numbers of money to sending (in BHT)
    output : fees of money sending
    limitation is 50,000BHT
    """
    total = input(); m_type = raw_input()
    if total > 50000:
        print "Limitation of sending is 50,000BHT"
    else:
        if m_type == "online":
            fees = 50; total = total / 10000.0
            if total % 1 == 0:
                total = int(total)
            else:
                total = int(total) + 1
            for i in range(1, total):
                fees += 10
        elif m_type == "ems" or m_type == "normal":
            if m_type == "ems":
                fees = 44.94
            elif m_type == "normal":
                fees = 10.7
            total = total / 1000.0
            if total % 1 == 0:
                total = int(total)
            else:
                total = int(total) + 1
            for i in range(1, total):
                fees += 2.14
        else:
            print "Please enter again"
            money()
        print "Total fees is:","%.02f" % fees, "BHT"
def about():
    """
    about window
    """
    w_about = Tk(); w_about.title("About")
    label1 = Label(w_about, text="PricePost, IT KMITL PSIT project")
    label2 = Label(w_about, text="Semaster 1, 2014")
    b_back = Button(w_about, text="Back to main window")
    label1.pack(); label2.pack(); b_back.pack()
    w_about.mainloop()
def main_prog():
    """
    main program
    """
    root = Tk(); root.title("PricePost")
    top_label = Label(root, text="Welcome to PricePost")
    btn_post = Button(root, text="Click here for postal")
    btn_parcel = Button(root, text="Click here for parcel", command=parcel_win)
    btn_trans = Button(root, text="Click here for money transfer", command=money)
    btn_about = Button(root, text="About", command=about)
    btn_exit = Button(root, text="Exit", command=w_exit)
    top_label.pack(); btn_post.pack(); btn_parcel.pack(); btn_trans.pack(); \
    btn_about.pack(); btn_exit.pack()
    root.mainloop()
main_prog()
