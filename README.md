# Africa Currency Formatter
This is a light weight python module to format African currencies

## Installation
NB: This module has been tested on python 3, but may not have
backward compactability with python 2

*We recommend you create a virtual enviroment*
> python3 -m venv env
> 
> source env/bin/activate
> 
> pip install format_afro_currency

## Demo
> format_afro_currency.currency(1000)
> 
> '₦1,000.00'
> 
> value = 1000
> 
> format_afro_currency.currency(value, currency='NGN', show_naira=True, show_kobo=False)
> 
> '₦1,000.00'

Currently this module provide support for the currency listed below,
but will have support have more african currencies in later version of this module.

Nigeria 				Nigerian naira 			NGN
