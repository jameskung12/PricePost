"""
Converting to OOP
"""
from Tkinter import *
def w_exit():
    """ window exit function """
    import sys; sys.exit()
class PricePost:
    def __init__(main_win):
        """ main program """
        main_win.root = Tk()
        main_win.root.title("PricePost")
        main_win.mw_lbl1 = Label(main_win.root, text="Welcome to PricePost").pack()
        main_win.btn_post = Button(main_win.root, text="Click here for postal").pack()
        main_win.btn_parcel = Button(main_win.root, text="Click here for parcel", command=main_win.parcel_win).pack()
        main_win.btn_trans = Button(main_win.root, text="Click here for money transfer").pack()
        main_win.btn_about = Button(main_win.root, text="About", command=main_win.about_win).pack()
        main_win.btn_exit = Button(main_win.root, text="Exit", command=w_exit).pack()
        main_win.root.mainloop()
    #def postal(fees=0):
    #def postal_win():
        #""" postal window """
        #postal = Tk()
        #postal.title("Postal sending calculation")
        #label1 = Label(postal, text="Please enter weight of postal (in kg)").pack()
        #w_entry = Entry(postal).pack()
        #label2 = Label(postal, text="Please select type").pack()
        #n_radio = Radiobutton(postal, text="Normal").pack()
        #r_radio = Radiobutton(postal, text="Registered").pack()
        #m_radio = Radiobutton(postal, text="EMS").pack()
        #e_button = Button(postal, text="Enter").pack()
        #label2 = Label(postal).pack()
        #postal.mainloop().pack()
    def parcel_win(main_win):
        """ parcel window """
        main_win.parcel = Tk()
        main_win.parcel.title("Parcel calculation")
        main_win.pa_weight = IntVar()
        main_win.paw_label1 = Label(main_win.parcel, text="Please enter weight (in kg)").pack()
        main_win.paw_w_entry = Entry(main_win.parcel, textvariable=main_win.pa_weight).pack()
        main_win.paw_e_button = Button(main_win.parcel, text="Enter", command=main_win.c_parcel).pack()
        main_win.paw_r_button = Button(main_win.parcel, text="Reset", command=main_win.parcel_res).pack()
        main_win.parcel.mainloop()
    def c_parcel(main_win):
        pa_calc = Parcel(main_win.pa_weight.get())
        res_call = pa_calc.parcel()
        main_win.paw_label2 = Label(main_win.parcel, text=res_call).pack()
    def parcel_res(main_win):
        main_win.parcel.destroy()
        main_win.parcel_win()
    #def money_win(main_win):
        #""" money window """
        #main_win.money = Tk()
        #main_win.money.title("Money sending calculation")
        #main_win.label1 = Label(main_win.money, text="Please enter total of money (in BHT)").pack()
        #main_win.mo_total = StrVar()
        #main_win.t_entry = Entry(main_win.money, textvariable=mo_total).pack()
        #main_win.label2 = Label(main_win.money, text="Please select type").pack()
        #main_win.n_radio = Radiobutton(main_win.money, text="Normal").pack()
        #main_win.e_radio = Radiobutton(main_win.money, text="EMS").pack()
        #main_win.o_radio = Radiobutton(main_win.money, text="Online").pack()
        #main_win.e_button = Button(main_win.money, text="Enter").pack()
        #main_win.label2 = Label(main_win.money).pack()
        #main_win.money.mainloop()
    #def c_money(main_win):
        #pa_calc = Money(main_win.mo_total.get())
        #res_call = pa_calc.parcel()
        #main_win.paw_label2 = Label(main_win.parcel, text=res_call).pack()
    def about_win(main_win):
        """ about window """
        main_win.w_about = Tk()
        main_win.w_about.title("About")
        main_win.label1 = Label(main_win.w_about, text="PricePost, IT KMITL PSIT project").pack()
        main_win.label2 = Label(main_win.w_about, text="Semaster 1, 2014").pack()
        main_win.label3 = Label(main_win.w_about).pack()
        main_win.label4 = Label(main_win.w_about).pack()
        main_win.label5 = Label(main_win.w_about).pack()
        main_win.w_about.mainloop()
class Parcel:
    def __init__(main_win, weight):
        main_win.pa_weight = weight
    def parcel(main_win):
        fees = 20
        if main_win.pa_weight > 20:
            return "Limitation of sending is 20kg"
            main_win.parcel.destroy()
            PricePost()
        else:
            if main_win.pa_weight % 1 == 0:
                main_win.pa_weight == int(main_win.pa_weight)
            else:
                main_win.pa_weight == int(main_win.pa_weight) + 1
            for i in xrange(1, main_win.pa_weight+1):
                fees += 15
            return "Total fees is : " + str(fees) + " BHT"
#class Money:
    #def __init__(main_win, m_total, m_type):

    #def money(m_total, fees=0):
        #if m_total > 50000:
            #print "Limitation of sending is 50,000BHT"
        #else:
            #if m_type == 3:
            #    fees = 50; m_total = m_total / 10000.0
            #    if m_total % 1 == 0:
            #        m_total = int(m_total)
            #    else:
            #        m_total = int(m_total) + 1
            #    for i in range(1, m_total):
            #        fees += 10
            #elif m_type == 1 or m_type == 2:
            #    if m_type == 2:
            #        fees = 44.94
            #    elif m_type == 1:
            #        fees = 10.7
            #    m_total = m_total / 1000.0
            #    if m_total % 1 == 0:
            #        m_total = int(m_total)
            #    else:
            #        m_total = int(m_total) + 1
            #    for i in range(1, m_total):
            #        fees += 2.14
            #return "Total fees is:","%.02f" % fees, "BHT"
PricePost()
