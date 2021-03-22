@staticmethod
def currency(value, show_naira=True, show_kobo=False):
    try:
        int(value)
    except Exception as e:
        return e
    try:
        naira = ""
        kobo = ""
        if show_naira is True:
            naira = "₦"
        if show_kobo is True:
            kobo = "K"
        currency_val = "{:0,.2f}".format(float(value))
        return "{0}{1}{2}".format(naira, currency_val, kobo)
        # if show_currency:
        #     return "{0}{:1,.2f}{3}".format(naira, float(1000000.05), kobo)
        # else:
        #     return "{:0,.2f}".format(float(1000000.05))
    except Exception as e:
        return "{0} \nSomething went wrong".format(e)
    except NameError as e:
        return "{0} \nSomething went wrong".format(e)
# NairaFormat.currency(1000)

