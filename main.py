from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>
<html lang="en-US">
    <body>
        <form action="/hello" method="POST">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name"/>
            <input type="submit"/>
        </form>
    </body>
</html>    
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=["POST"])
def hello():
    firstname = request.form["first_name"]
    return "<h1>Hello, " + firstname + ". Enjoy your stay!</h1>"   

app.run()    