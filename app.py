from flask import Flask, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_home_page():


    return render_template("home.html")


@app.route("/convert")
def show_convert_page():


    # Figure out how to convert
    # Get rates from the .get_rates
    # Create the equations to convert for each currency
    # Amount of the "Convert from" multiplied by the "Convert to" rates listed form the .get_rates
    #


    # Gets the currency Symbol
    # cCode= CurrencyCodes()
    # cCode.get_symbol("GBP")

    c = CurrencyRates()

    #All the request.args are from the home.html's input names
    #It was in the url parameters and we're able to copy the parameter's name onto the new page
    convert_from = request.args["convert_from"]
    convert_to = request.args["convert_to"]
    amount = request.args["amount"]


    # using the forex converter terminology, I used .convert to convert the given currency to the target currency
    # Ex. convert_from (USD), convert_to (GBP), amount(50) - had to convert to an integer by using int(amount)
    new_amount = c.convert(convert_from, convert_to, int(amount))

    brandnew_amount = round(new_amount, 2)

    # Getting Symbols for both of the currencies
    cc = CurrencyCodes()

    convert_from_symbol = cc.get_symbol(convert_from)
    convert_to_symbol = cc.get_symbol(convert_to)

   
    
    return render_template("convert.html", convert_from=convert_from, convert_to=convert_to, amount=amount, brandnew_amount=brandnew_amount, convert_from_symbol=convert_from_symbol, convert_to_symbol=convert_to_symbol)

## Next Step: Find out how to do error messages: Convert from, convert to, and amount
## -Probably have to do conditional logic: if it doesn't = the key, or for loop to go over each key
## -Flash Messages???
## -Create a div or message that's stored in cookie or sessions???

## Decorate???
## At least make the form and button look neater/clean
## Make the button blue w/ White Font, rounded edges
## Font Style?
## Should i make selected form input have a thick gray border to indicated that it's being selected???
