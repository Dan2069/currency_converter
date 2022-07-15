
from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes




app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route("/")
def show_home_page():


    return render_template("home.html")

@app.route("/convert", methods = ["GET", "POST"])
def show_convert_page():


    if request.method == "GET":
        return "I just did a get request"


    if request.method == "POST":
        convert_from = request.form["convert_from"]
        convert_to = request.form["convert_to"]
        amount = request.form["amount"]

        c = CurrencyRates()

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


        if amount.isdigit() == False:
            # if len(amount) == 0:
            #     flash("Please fill in this field") 
            # else: 
                flash(f"Please enter a valid amount (i.e. No spaces or negative numbers). You have entered '{amount}'.") # Will say it's invalid if it's not a number or if it's negative
                return redirect("/")

            # Unable to figure out a way to incorporate an error message if the "amount" form was submitted empty like convert_from and convert_to

        d = int(amount)
    
        conversion = c.convert(convert_from, convert_to, d)

        new_amount = round(conversion, 2)

        cc = CurrencyCodes()

        convert_from_symbol = cc.get_symbol(convert_from)
        convert_to_symbol = cc.get_symbol(convert_to)

        return render_template("convert.html", convert_from=convert_from, convert_to=convert_to, amount=amount, new_amount=new_amount, convert_from_symbol=convert_from_symbol, convert_to_symbol=convert_to_symbol)

## Should i make it more pretty?
## Answer Conceptual Questions
## Write tests for my routes and functions