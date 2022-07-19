
from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes




app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


c = CurrencyRates()
cc = CurrencyCodes()

@app.route("/")
def show_home_page():
    """Displays the main page and form"""

    return render_template("home.html")

class cls_currency:
    """ Class that defines methods to convert and add the currency symbols"""

    def __init__(self, convert_from, convert_to, amount):
        self.convert_form = convert_from
        self.convert_to = convert_to
        self.amount = amount
    
    def my_convert(convert_from, convert_to, amount):
        """ Converts the original currency to the new currency using the Forex_python_converter """

        conversion = c.convert(convert_from, convert_to, amount)

        return round(conversion, 2)

    def my_symbol(convert_from, convert_to):
        """Obtains the symbols from the original and requested currencies"""
        
        convert_from_symbol = cc.get_symbol(convert_from)
        convert_to_symbol = cc.get_symbol(convert_to)

        pair = [convert_from_symbol, convert_to_symbol]

        return pair

@app.route("/convert", methods = ["GET", "POST"])
def show_convert_page():


    if request.method == "GET":
        return "I just did a get request"


    if request.method == "POST":

        convert_from = request.form["convert_from"]
        convert_to = request.form["convert_to"]
        amount = int(request.form["amount"])

        b = c.get_rates('USD') #Gets the converted rates of USD
        b['USD'] = 1 # Adds USD to the list of keys (currencies) & assigns it 1 as a value just incase both currencies are the same
        full_currency_list = b.keys() # Getting all the keys (EUR, USD, GBP etc.)

        if convert_from not in full_currency_list: #if the converted_to isn't apart of the list, sends back to original page w/ flash that it's invalid
            if len(convert_from) == 0: #This checks to see if it was empty
                flash("Please fill in this field")
            else: flash(f"{convert_from} is not a valid currency. Please try again")


        if convert_to not in full_currency_list or len(convert_to) == 0: #if the converted_from isn't apart of the list, sends back to original page w/ flash that it's invalid
            if len(convert_to) == 0: #This checks to see if it was empty
                flash("Please fill in this field")
            else: flash(f"{convert_to} is not a valid currency. Please try again")


        if str(amount).isdigit() == False:
                flash(f"Please enter a valid amount (i.e. No spaces or negative numbers). You have entered '{amount}'.") # Will say it's invalid if it's not a number or if it's negative
                return redirect("/")

        new_amount = cls_currency.my_convert(convert_from, convert_to, amount) # Calculates the converted amount
        symbol_1 = cls_currency.my_symbol(convert_from, convert_to)[0] # Gets the currency symbol from the convert_from
        symbol_2 = cls_currency.my_symbol(convert_from, convert_to)[1] # Gets the currency symbol from the convert_to

        return render_template("convert.html", convert_from_symbol = symbol_1, convert_from = convert_from, amount = amount, convert_to = convert_to, convert_to_symbol = symbol_2, new_amount = new_amount)