# @staticmethod
def currency(value, currency='NGN', show_naira=True, show_kobo=False):
    try:
        int(value)
    except Exception as e:
        return e
    try:
        naira = ""
        kobo = ""
        if currency == 'NGN':
            if show_naira is True:
                naira = "₦"
            if show_kobo is True:
                kobo = "K"
        else:
            raise lueError '{0} currency is not available'.format(currency)
        currency_val = "{:0,.2f}".format(float(value))
        return "{0}{1}{2}".format(naira, currency_val, kobo)
    except Exception as e:
        return "{0} \nSomething went wrong".format(e)
    except NameError as e:
        return "{0} \nSomething went wrong".format(e)
# NairaFormat.currency(1000)
