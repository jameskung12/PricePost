"""
Bug fix on parcel window result display
"""
from Tkinter import *
def w_exit():
    """ window exit function """
    import sys; sys.exit()
class PricePost(object):
    def __init__(main_win):
        """ main program """
        main_win.root = Tk()
        main_win.root.title("PricePost")
        main_win.mw_lbl1 = Label(main_win.root, text="Welcome to PricePost").pack()
        main_win.btn_post = Button(main_win.root, text="Click here for postal and EMS", command=main_win.postal_win).pack()
        main_win.btn_parcel = Button(main_win.root, text="Click here for normal parcel", command=main_win.parcel_win).pack()
        main_win.btn_trans = Button(main_win.root, text="Click here for money transfer",command=main_win.money_win).pack()
        main_win.btn_about = Button(main_win.root, text="About", command=main_win.about_win).pack()
        main_win.btn_exit = Button(main_win.root, text="Exit", command=w_exit).pack()
        main_win.root.mainloop()
    def postal_win(main_win):
        """ postal window """
        main_win.postal = Tk()
        main_win.postal.title("Postal sending calculation")
        main_win.pow_label1 = Label(main_win.postal, text="Please enter weight of postal (or parcel in case of EMS) (in g)").pack()
        main_win.po_weight = IntVar()
        main_win.po_weight = Entry(main_win.postal, textvariable=main_win.po_weight)
        main_win.po_weight.pack()
        main_win.pow_label2 = Label(main_win.postal, text="Please select type").pack()
        main_win.po_type = IntVar()
        main_win.pow_redio1 = Radiobutton(main_win.postal, text="Normal" ,variable=main_win.po_type, value=1)
        main_win.pow_redio2 = Radiobutton(main_win.postal, text="Registered", variable=main_win.po_type, value=2)
        main_win.pow_redio3 = Radiobutton(main_win.postal, text="EMS", variable=main_win.po_type, value=3)
        main_win.pow_redio1.pack()
        main_win.pow_redio2.pack()
        main_win.pow_redio3.pack()
        main_win.pow_e_button = Button(main_win.postal, text="Enter", command=main_win.c_postal).pack()
        main_win.pow_r_button = Button(main_win.postal, text="Reset", command=main_win.postal_res).pack()
        main_win.postal.mainloop()
    def c_postal(main_win):
        po_calc = Postal(main_win.po_weight.get(), main_win.po_type.get())
        res_call = po_calc.parcel()
        main_win.paw_label2 = Label(main_win.postal, text=res_call).pack()
    def postal_res(main_win):
        main_win.postal.destroy()
        main_win.postal_win()
    def parcel_win(main_win):
        """ parcel window """
        main_win.parcel = Tk()
        main_win.parcel.title("Parcel calculation")
        main_win.paw_label1 = Label(main_win.parcel, text="Please enter weight (in kg)").pack()
        main_win.pa_weight = IntVar()
        main_win.pa_weight = Entry(main_win.parcel, textvariable=main_win.pa_weight)
        main_win.pa_weight.pack()
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
    def money_win(main_win):
        """ money window """
        main_win.money = Tk()
        main_win.money.title("Money sending calculation")
        main_win.mw_label1 = Label(main_win.money, text="Please enter total of money (in BHT)").pack()
        main_win.mo_total = IntVar()
        main_win.mo_type = IntVar()
        main_win.mo_total = Entry(main_win.money, textvariable=main_win.mo_total)
        main_win.mo_total.pack()
        main_win.mw_label2 = Label(main_win.money, text="Please select type").pack()
        main_win.redio1 = Radiobutton(main_win.money, text="Normal" ,variable=main_win.mo_type, value=1)
        main_win.redio2 = Radiobutton(main_win.money, text="EMS", variable=main_win.mo_type, value=2)
        main_win.redio3 = Radiobutton(main_win.money, text="Online", variable=main_win.mo_type, value=3)
        main_win.redio1.pack(); main_win.redio2.pack(); main_win.redio3.pack()
        main_win.mw_e_button = Button(main_win.money, text="Enter", command=main_win.c_money).pack()
        main_win.mw_r_button = Button(main_win.money, text="Reset", command=main_win.money_res).pack()
        main_win.money.mainloop()
    def c_money(main_win):
        mo_calc = Money(main_win.mo_total.get(), main_win.mo_type.get())
        res_call = mo_calc.money()
        main_win.paw_label2 = Label(main_win.money, text=res_call).pack()
    def money_res(main_win):
        main_win.money.destroy()
        main_win.money_win()
    def about_win(main_win):
        """ about window """
        main_win.w_about = Tk()
        main_win.w_about.title("About")
        main_win.aw_label1 = Label(main_win.w_about, text="PricePost, IT KMITL PSIT project").pack()
        main_win.aw_label2 = Label(main_win.w_about, text="Semaster 1, 2014").pack()
        main_win.aw_label3 = Label(main_win.w_about).pack()
        main_win.aw_label4 = Label(main_win.w_about).pack()
        main_win.aw_label5 = Label(main_win.w_about).pack()
        main_win.aw_close = Button(main_win.w_about, text="Close", command=main_win.win_close).pack()
        main_win.w_about.mainloop()
    def win_close(main_win):
        main_win.w_about.destroy()
class Postal():
    def __init__(main_win, p_weight, p_type):
        main_win.po_weight = int(p_weight)
        main_win.po_type = int(p_type)
    def parcel(main_win, fees=0):
        return main_win.po_weight
class Parcel():
    def __init__(main_win, weight):
        main_win.pa_weight = int(weight)
    def parcel(main_win):
        if main_win.pa_weight> 20:
            return "Limitation of sending is 20kg"
        elif main_win.pa_weight<= 0:
            return "minimum is 0.1 kg"
        elif main_win.pa_weight > 0 or main_win.pa_weight <= 20:
            fees = 20
            for i in range(1, main_win.pa_weight):
                fees += 15
            return "Total fees is : " + str(fees) + " BHT"
        else:
            return "Error, try again"
class Money:
    def __init__(main_win, m_total, m_type):
        main_win.mo_total = int(m_total)
        main_win.mo_type = int(m_type)
    def money(main_win, fees=0):
        #return main_win.mo_type
        if main_win.mo_total > 50000:
            return "Limitation of sending is 50,000BHT"
        else:
            #if main_win.mo_type == 3:
                #fees = 50; main_win.mo_total = int(main_win.mo_total / 10000)
                #for i in range(1, main_win.mo_total+1):
                    #fees += 10
            #elif main_win.mo_type == 1 or main_win.mo_type == 2:
                #if main_win.mo_type == 1:
            fees = 10.7
                #elif main_win.mo_type == 2:
                    #fees = 44.94
            main_win.mo_total = int(main_win.mo_total / 1000)
            for i in range(1, main_win.mo_total+1):
                fees += 2.14
            return "Total fees is : " + "%.02f" % fees + " BHT"
PricePost()
