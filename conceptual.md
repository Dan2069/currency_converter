### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

- Python is typically the language for Backend development and JavaScript is typically the langauge for Frontend.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  You can use get() to see if "c" is in the dictionary and pass in a value like "None" for its value
  You can also use setdefault() or defaultdict, but it will fill in the default value for every missing key

- What is a unit test?

  A Unit test is code to test a specific funtion or method of our app

- What is an integration test?

  An Integration test is code that tests if the methods and functions work together

- What is the role of web application framework, like Flask?

- The role of the web application framework is to simplify and create and easier way to create pages that would have taken a very long time

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  If you're trying to get resource information for a specific route, using the parameter in the route URL is prefered.
  If you're simply trying to filter through the information, using the URL query param is prefered. 

- How do you collect data from a URL placeholder parameter using Flask?

  You can collect data from a URL placeholder by using the request.args['<argument name>'] 

- How do you collect data from the query string using Flask?

  You can collect data form the query string by using the request.args.get()

- How do you collect data from the body of the request using Flask?

  You can collect data from the body of the request by using request.form() which are key/value pairs in the body

- What is a cookie and what kinds of things are they commonly used for?

  Cookies are small bits of informations thats stored in the browser. They're commonly used for remembering session information and tracking items for the user

- What is the session object in Flask?

  The session object in Flask is an object that tracks the session variables and their values

- What does Flask's `jsonify()` do?

  Flasks's 'jsonify()' converts json to response objects, but it adds a the dumps() function
