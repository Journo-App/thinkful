#there is a copy of this in my gdi_thinkful>Flask dir == hello_world_flask.py

from flask import Flask 
from os import environ

app = Flask(__name__) 

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())


@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname,lastname):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(lastname[0:3].title()+firstname[0:2].title())
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            