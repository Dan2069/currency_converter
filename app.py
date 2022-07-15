
from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes




app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_home_page():


    return render_template("home.html")



# @app.route("/new")
# def check_home_page():

#     convert_from = request.form["convert_from"]
#     convert_to = request.form["convert_to"]
#     amount = request.form["amount"]

#     flash(f"This is the convert_from variable {convert_from}")
#     flash(f"This is the convert_to variable {convert_to}")
#     flash(f"This is the amount variable {amount}")

#     return redirect("/test", convert_from=convert_from, convert_to=convert_to, amount=amount)


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
            flash(f"{convert_from} is not a valid currency. Please try again")

        if convert_to not in full_currency_list: #if the converted_from isn't apart of the list, sends back to original page w/ flash that it's invalid
            flash(f"{convert_to} is not a valid currency. Please try again")


        if amount.isdigit() == False:
            flash(f"{amount} is not a valid amount. Please enter a valid amount") # Will say it's invalid if it's not a number or if it's negative
            return redirect("/")
    
        conversion = c.convert(convert_from, convert_to, int(amount))

        new_amount = round(conversion, 2)

        cc = CurrencyCodes()

        convert_from_symbol = cc.get_symbol(convert_from)
        convert_to_symbol = cc.get_symbol(convert_to)

        return render_template("convert.html", convert_from=convert_from, convert_to=convert_to, amount=amount, new_amount=new_amount, convert_from_symbol=convert_from_symbol, convert_to_symbol=convert_to_symbol)




@app.route("/test")
def test_parameters():
    c = CurrencyRates()
    b = c.get_rates('USD')
    b['USD'] = 1
    res = b.keys()
    
    return (str(res))

## Next Step: Find out how to do error messages: Convert from, convert to, and amount
## -Probably have to do conditional logic: if it doesn't = the key, or for loop to go over each key
## -Flash Messages???
## -Create a div or message that's stored in cookie or sessions???

## Decorate???
## At least make the form and button look neater/clean
## Make the button blue w/ White Font, rounded edges
## Font Style?
## Should i make selected form input have a thick gray border to indicated that it's being selected???
