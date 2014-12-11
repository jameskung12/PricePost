"""
Added all windows
"""
from Tkinter import *
def w_exit():
    """ window exit function """
    import sys; sys.exit()
def postal_win():
    """ postal window """
    postal = Tk()
    postal.title("Postal sending calculation")
    label1 = Label(postal, text="Please enter weight of postal (in kg)").pack()
    w_entry = Entry(postal).pack()
    label2 = Label(postal, text="Please select type").pack()
    n_radio = Radiobutton(postal, text="Normal").pack()
    r_radio = Radiobutton(postal, text="Registered").pack()
    m_radio = Radiobutton(postal, text="EMS").pack()
    e_button = Button(postal, text="Enter").pack()
    postal.mainloop()
def parcel_win():
    """ parcel window """
    parcel = Tk()
    parcel.title("Parcel calculation")
    label1 = Label(parcel, text="Please enter weight (in kg)").pack()
    w_entry = Entry(parcel).pack()
    e_button = Button(parcel, text="Enter").pack()
    parcel.mainloop()
def money_win():
    """ money window """
    money = Tk()
    money.title("Money sending calculation")
    label1 = Label(money, text="Please enter total of money (in BHT)").pack()
    t_entry = Entry(money).pack()
    label2 = Label(money, text="Please select type").pack()
    n_radio = Radiobutton(money, text="Normal").pack()
    e_radio = Radiobutton(money, text="EMS").pack()
    o_radio = Radiobutton(money, text="Online").pack()
    e_button = Button(money, text="Enter").pack()
    money.mainloop()
#def postal(fees=0):
#def parcel(fees=20):
    #weight = input()
    #if weight > 20:
        #print "Limitation of sending is 20kg"
    #else:
        #if weight % 1 == 0:
            #weight == int(weight)
        #else:
            #weight == int(weight) + 1
        #for i in range(1, int(weight) + 1):
            #fees += 15
        #print "Total fees is:", fees, "BHT"
#def money(fees=0):
    #total = input(); m_type = raw_input()
    #if total > 50000:
        #print "Limitation of sending is 50,000BHT"
    #else:
        #if m_type == "online":
        #    fees = 50; total = total / 10000.0
        #    if total % 1 == 0:
        #        total = int(total)
        #    else:
        #        total = int(total) + 1
        #    for i in range(1, total):
        #        fees += 10
        #elif m_type == "ems" or m_type == "normal":
        #    if m_type == "ems":
        #        fees = 44.94
        #    elif m_type == "normal":
        #        fees = 10.7
        #    total = total / 1000.0
        #    if total % 1 == 0:
        #        total = int(total)
        #    else:
        #        total = int(total) + 1
        #    for i in range(1, total):
        #        fees += 2.14
        #else:
        #    print "Please enter again"
        #    money()
        #print "Total fees is:","%.02f" % fees, "BHT"
def about_win():
    """ about window """
    w_about = Tk()
    w_about.title("About")
    label1 = Label(w_about, text="PricePost, IT KMITL PSIT project").pack()
    label2 = Label(w_about, text="Semaster 1, 2014").pack()
    w_about.mainloop()
def main_prog():
    """ main program """
    root = Tk()
    root.title("PricePost")
    top_label = Label(root, text="Welcome to PricePost").pack()
    btn_post = Button(root, text="Click here for postal", command=postal_win).pack()
    btn_parcel = Button(root, text="Click here for parcel", command=parcel_win).pack()
    btn_trans = Button(root, text="Click here for money transfer", command=money_win).pack()
    btn_about = Button(root, text="About", command=about_win).pack()
    btn_exit = Button(root, text="Exit", command=w_exit).pack()
    root.mainloop()
main_prog()
