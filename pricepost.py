"""
PricePost, IT KMITL project Version 0.01 alpha
"""
from Tkinter import *
def w_exit():
    """Program exit function"""
    import sys; sys.exit()
class PricePost(object):
    def __init__(price_post):
        """Main window"""
        price_post.root = Tk()
        price_post.root.title("PricePost, IT KMITL project (Version 0.01 alpha)")
        price_post.mw_lbl1 = Label(price_post.root, text="Welcome to PricePost").pack()
        price_post.btn_post = Button(price_post.root, text="Click here for postal and EMS", command=price_post.postal_win).pack()
        price_post.btn_parcel = Button(price_post.root, text="Click here for normal parcel", command=price_post.parcel_win).pack()
        price_post.btn_trans = Button(price_post.root, text="Click here for money transfer",command=price_post.money_win).pack()
        price_post.btn_about = Button(price_post.root, text="About", command=price_post.about_win).pack()
        price_post.btn_exit = Button(price_post.root, text="Exit", command=w_exit).pack()
        price_post.root.mainloop()
    def postal_win(price_post):
        """Postal window"""
        price_post.postal = Tk()
        price_post.postal.title("Postal sending calculation")
        price_post.pow_label1 = Label(price_post.postal, text="Please enter weight of postal (or parcel in case of EMS) (in g)").pack()
        price_post.po_weight = IntVar()
        price_post.po_weight = Entry(price_post.postal, textvariable=price_post.po_weight)
        price_post.po_weight.pack()
        #price_post.pow_label2 = Label(price_post.postal, text="Please select type").pack()
        price_post.po_type = IntVar()
        #price_post.pow_radio1 = Radiobutton(price_post.postal, text="Normal" ,variable=price_post.po_type, value=1).pack()
        #price_post.pow_radio2 = Radiobutton(price_post.postal, text="Registered", variable=price_post.po_type, value=2).pack()
        #price_post.pow_radio3 = Radiobutton(price_post.postal, text="EMS", variable=price_post.po_type, value=3).pack()
        price_post.pow_e_button = Button(price_post.postal, text="Enter", command=price_post.c_postal).pack()
        price_post.pow_r_button = Button(price_post.postal, text="Reset", command=price_post.postal_res).pack()
        price_post.postal.mainloop()
    def c_postal(price_post):
        po_calc = Postal(price_post.po_weight.get(), price_post.po_type.get())
        res_call = po_calc.postal()
        price_post.paw_label2 = Label(price_post.postal, text=res_call).pack()
    def postal_res(price_post):
        price_post.postal.destroy()
        price_post.postal_win()
    def parcel_win(price_post):
        """Parcel window"""
        price_post.parcel = Tk()
        price_post.parcel.title("Parcel calculation")
        price_post.paw_label1 = Label(price_post.parcel, text="Please enter weight (in kg)").pack()
        price_post.pa_weight = IntVar()
        price_post.pa_weight = Entry(price_post.parcel, textvariable=price_post.pa_weight)
        price_post.pa_weight.pack()
        price_post.paw_e_button = Button(price_post.parcel, text="Enter", command=price_post.c_parcel).pack()
        price_post.paw_r_button = Button(price_post.parcel, text="Reset", command=price_post.parcel_res).pack()
        price_post.parcel.mainloop()
    def c_parcel(price_post):
        """Call parcel class and return value"""
        pa_calc = Parcel(price_post.pa_weight.get())
        res_call = pa_calc.parcel()
        price_post.paw_label2 = Label(price_post.parcel, text=res_call).pack()
    def parcel_res(price_post):
        """Reset parcel window"""
        price_post.parcel.destroy()
        price_post.parcel_win()
    def money_win(price_post):
        """Money window"""
        price_post.money = Tk()
        price_post.money.title("Money sending calculation")
        price_post.mw_label1 = Label(price_post.money, text="Please enter total of money (in BHT)").pack()
        price_post.mo_total = IntVar()
        price_post.mo_total = Entry(price_post.money, textvariable=price_post.mo_total)
        price_post.mo_total.pack()
        #price_post.mw_label2 = Label(price_post.money, text="Please select type").pack()
        price_post.mo_type = IntVar()
        #price_post.mo_radio1 = Radiobutton(price_post.money, text="Normal", variable=price_post.mo_type, value=1).pack()
        #price_post.mo_radio2 = Radiobutton(price_post.money, text="EMS", variable=price_post.mo_type, value=2).pack()
        #price_post.mo_radio3 = Radiobutton(price_post.money, text="Online", variable=price_post.mo_type, value=3).pack()
        price_post.mw_e_button = Button(price_post.money, text="Enter", command=price_post.c_money).pack()
        price_post.mw_r_button = Button(price_post.money, text="Reset", command=price_post.money_res).pack()
        price_post.money.mainloop()
    def c_money(price_post):
        """Call money class and return value"""
        mo_calc = Money(price_post.mo_total.get(), price_post.mo_type.get())
        res_call = mo_calc.money()
        price_post.mw_label2 = Label(price_post.money, text=res_call).pack()
    def money_res(price_post):
        """Reset money window"""
        price_post.money.destroy()
        price_post.money_win()
    def about_win(price_post):
        """About window"""
        price_post.w_about = Tk()
        price_post.w_about.title("About")
        price_post.aw_label1 = Label(price_post.w_about, text="PricePost, IT KMITL PSIT project").pack()
        price_post.aw_label2 = Label(price_post.w_about, text="Version 0.01 alpha, Developed by").pack()
        price_post.aw_label3 = Label(price_post.w_about, text="Palit Wiboonlit, 57070085").pack()
        price_post.aw_label4 = Label(price_post.w_about, text="57").pack()
        price_post.aw_label5 = Label(price_post.w_about, text="Semaster 1, 2014").pack()
        price_post.aw_close = Button(price_post.w_about, text="Close", command=price_post.aw_close).pack()
        price_post.w_about.mainloop()
    def aw_close(price_post):
        """Close about window"""
        price_post.w_about.destroy()
class Postal():
    def __init__(price_post, p_weight, p_type):
        """Calling postal weight and type value"""
        price_post.po_weight = int(p_weight)
        price_post.po_type = int(p_type)
    def postal(price_post, fees=0):
        """Calculation"""
        return price_post.po_weight
class Parcel():
    def __init__(price_post, weight):
        """Calling parcel weight value"""
        price_post.pa_weight = int(weight)
    def parcel(price_post):
        """Calculation"""
        if price_post.pa_weight > 20:
            return "Limitation of sending is 20 kg"
        elif price_post.pa_weight > 0 or price_post.pa_weight <= 20:
            fees = 20
            for i in range(1, price_post.pa_weight):
                fees += 15
            return "Total fees is : " + str(fees) + " BHT"
        else:
            return "Error, try again"
class Money():
    def __init__(price_post, m_total, m_type):
        """Calling money to send and type value"""
        price_post.mo_total = int(m_total)
        price_post.mo_type = m_type
    def money(price_post, fees=0):
        """Calculation"""
        if price_post.mo_total > 50000:
            return "Limitation of sending is 50,000 BHT"
        elif price_post.mo_total >= 1 and price_post.mo_total <= 50000:
            return price_post.mo_total
            #if price_post.mo_radio == 3:
                #fees = 50; price_post.mo_total = int(price_post.mo_total / 10000)
                #for i in range(1, price_post.mo_total+1):
                    #fees += 10
            #elif price_post.mo_radio == 1 or price_post.mo_radio == 2:
                #if price_post.mo_radio == 1:
                    #fees = 10.7
                #elif price_post.mo_radio == 2:
                    #fees = 44.94
                #price_post.mo_total = int(price_post.mo_total / 1000)
            #for i in range(1, price_post.mo_total+1):
                #fees += 2.14
            #return "Total fees is : " + "%.02f" % fees + " BHT"
        else:
            return "Error, try again"
PricePost()
