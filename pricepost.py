"""
PricePost, IT KMITL project Version 0.02 alpha
"""
from Tkinter import *
def w_exit():
    """Program exit function"""
    import sys; sys.exit()
"""Class for main window"""
class PricePost(object):
    def __init__(price_post):
        """Main window"""
        price_post.root = Tk()
        price_post.root.title("PricePost, IT KMITL project")
        price_post.root.geometry("224x160")
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
        price_post.pow_label2 = Label(price_post.postal, text="Please enter type (Normal, Registered, EMS)").pack()
        price_post.po_type = StringVar()
        price_post.po_type = Entry(price_post.postal, textvariable=price_post.po_type)
        price_post.po_type.pack()
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
        price_post.parcel.geometry("160x128")
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
        price_post.mw_label2 = Label(price_post.money, text="Please enter type (Normal, EMS, Online)").pack()
        price_post.mo_type = StringVar()
        price_post.mo_type = Entry(price_post.money, textvariable=price_post.mo_type)
        price_post.mo_type.pack()
        price_post.mw_e_button = Button(price_post.money, text="Enter", command=price_post.c_money).pack()
        price_post.mw_r_button = Button(price_post.money, text="Reset", command=price_post.money_res).pack()
        price_post.money.mainloop()
    def c_money(price_post):
        """Call money class and return value"""
        mo_calc = Money(price_post.mo_total.get(), price_post.mo_type.get())
        res_call = mo_calc.money()
        price_post.mw_label3 = Label(price_post.money, text=res_call).pack()
    def money_res(price_post):
        """Reset money window"""
        price_post.money.destroy()
        price_post.money_win()
    def about_win(price_post):
        """About window"""
        price_post.w_about = Tk()
        price_post.w_about.title("About")
        price_post.aw_label1 = Label(price_post.w_about, text="PricePost, IT KMITL PSIT project").pack()
        price_post.aw_label2 = Label(price_post.w_about, text="Version 1.0, Developed by :").pack()
        price_post.aw_label3 = Label(price_post.w_about, text="Palit Wiboonlit, ID 57070085").pack()
        price_post.aw_label4 = Label(price_post.w_about, text="Pachara Pinyopornpanich, ID 55070076").pack()
        price_post.aw_label5 = Label(price_post.w_about, text="Semaster 1, 2014").pack()
        price_post.aw_close = Button(price_post.w_about, text="Close", command=price_post.aw_close).pack()
        price_post.w_about.mainloop()
    def aw_close(price_post):
        """Close about window"""
        price_post.w_about.destroy()
"""Class for postal calculation"""
class Postal():
    def __init__(price_post, p_weight, p_type):
        """Calling postal weight and type value"""
        price_post.po_weight = int(p_weight)
        price_post.po_type = str(p_type)
    def postal(price_post, fees=0):
        """Calculation"""
        if price_post.po_weight <= 20:
            price_post.po_weight = 1
        else:
            if price_post.po_weight <= 100:
                price_post.po_weight = 2
            elif price_post.po_weight <= 250:
                price_post.po_weight = 3
            elif price_post.po_weight <= 500:
                price_post.po_weight = 4
            elif price_post.po_weight > 500:
                price_post.po_weight = price_post.po_weight / 500.0
                if price_post.po_weight == 1:
                    price_post.po_weight = 5
                elif price_post.po_weight % 1 == 0:
                    price_post.po_weight = (int(price_post.po_weight) - 1) + 4
                else:
                    price_post.po_weight = int(price_post.po_weight) + 4
        if price_post.po_type == "ems" or  price_post.po_type == "EMS":
            fees = 32
            num = 5
            if price_post.po_weight > 23:
                return "Error, try again"
            else:
                for i in range(1,  price_post.po_weight):
                    if i == 1 or i == 2 or i == 3:
                        if i == 3:
                            num = 10
                        else:
                            num = 5
                    elif i == 4 or i == 5 or i == 6 or i == 8:
                        num = 15
                    elif i == 9 or i == 10 or i == 11 or i == 12:
                        num = 20
                    elif i == 19 or i == 20 or i == 21 or i == 22 or i == 23:
                        num = 30
                    else:
                        num = 25
                    fees += num
                return "Total fees is : " + "%.02f" % fees + " BHT"
            
        elif price_post.po_type == "Registered" or price_post.po_type == "registered"\
         or price_post.po_type == "Normal" or price_post.po_type == "normal":
            if price_post.po_weight <= 7 :
                if price_post.po_type == "Registered" or price_post.po_type == "registered":
                    fees = 16
                    num = 2
                    for i in range(1, price_post.po_weight):
                        fees += num
                        if i >= 3:
                            if i >= 4:
                                num = 20
                                if i >= 5:
                                    num -= 20
                            else:
                                num = 10
                        else:
                            num += 2
                elif price_post.po_type == "Normal" or price_post.po_type == "normal":
                    fees = 3
                    num = 2
                    for i in range(1, price_post.po_weight):
                        fees += num
                        if i >= 3:
                            if i >= 4:
                                num = 20
                                if i >= 5:
                                    num -= 20
                            else:
                                num = 10
                        else:
                            num += 2
                return "Total fees is : " + "%.02f" % fees + " BHT"
            else:
                return "Error, try again"
"""Class for parcel calculation"""
class Parcel():
    def __init__(price_post, weight):
        """Calling parcel weight value"""
        price_post.pa_weight = int(weight)
    def parcel(price_post):
        """Calculation"""
        if price_post.pa_weight > 20:
            return "Limitation of sending is 20 kg"
        elif price_post.pa_weight > 0 and price_post.pa_weight <= 20:
            fees = 20
            for i in range(1, price_post.pa_weight):
                fees += 15
            return "Total fees is : " + "%.02f" % fees + " BHT"
        else:
            return "Error, try again"
"""Class for money calculation"""
class Money():
    def __init__(price_post, m_total, m_type):
        """Calling money to send and type value"""
        price_post.mo_total = int(m_total)
        price_post.mo_type = str(m_type)
    def money(price_post, fees=0):
        """Calculation"""
        if price_post.mo_total > 50000:
            return "Limitation of sending is 50,000 BHT"
        elif price_post.mo_total >= 1 and price_post.mo_total <= 50000:
            if price_post.mo_type == "Online" or price_post.mo_type == "online":
                fees = 50
                if price_post.mo_total % 10000 == 0:
                    price_post.mo_total = int(price_post.mo_total / 10000)
                    for i in range(1, price_post.mo_total):
                        fees += 10
                else:
                    price_post.mo_total = int(price_post.mo_total / 10000)
                    for i in range(1, price_post.mo_total+1):
                        fees += 10
                return "Total fees is : " + "%.02f" % fees + " BHT"
            elif price_post.mo_type == "Normal" or price_post.mo_type == "normal"\
                 or price_post.mo_type == "EMS" or price_post.mo_type == "ems":
                if price_post.mo_type == "Normal" or price_post.mo_type == "normal":
                    fees = 10.7
                elif price_post.mo_type == "EMS" or price_post.mo_type == "ems":
                    fees = 44.94
                if price_post.mo_total % 1000 == 0:
                    price_post.mo_total = int(price_post.mo_total / 1000)
                    for i in range(1, price_post.mo_total):
                        fees += 2.14
                else:
                    price_post.mo_total = int(price_post.mo_total / 1000)
                    for i in range(1, price_post.mo_total+1):
                        fees += 2.14
                return "Total fees is : " + "%.02f" % fees + " BHT"
            else:
                return "Error, try again"
        else:
            return "Error, try again"
PricePost()
