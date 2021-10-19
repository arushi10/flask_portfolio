# import "packages" from flask
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
#import "packages" from flask
from flask import Flask, render_template, request
from image import image_data, prisha_image_data, arushi_image_data, vaishavi_image_data, siya_image_data
import requests


# create a Flask instance
app = Flask(__name__)


# connects default URL of server to render kangaroos.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/arushi/', methods=['GET', 'POST'])
def arushi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("arushi.html", name1=name)
    # starting and empty input default
    return render_template("arushi.html", name1="TechFish User")

@app.route('/AboutUs/', methods=['GET', 'POST'])
def AboutUs():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("MainAboutUs.html", name1=name)
    # starting and empty input default
    return render_template("MainAboutUs.html", name1="TechFish User")


@app.route('/prisha/', methods=['GET', 'POST'])
def prisha():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("prisha.html", name1=name)
    # starting and empty input default
    return render_template("prisha.html", name1="TechFish User")


@app.route('/vai/', methods=['GET', 'POST'])
def vai():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("vai.html", name1=name)
    # starting and empty input default
    return render_template("vai.html", name1="TechFish User")


@app.route('/siya/', methods=['GET', 'POST'])
def siya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("siya.html", name1=name)
    # starting and empty input default
    return render_template("siya.html", name1="TechFish User")


@app.route("/binary", methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
        # starting and empty input default
    return render_template("binary.html", bits=8)


@app.route('/mini_labs/')
def mini_labs():
    return render_template("mini_labs.html")


@app.route('/explore/', methods=['GET', 'POST'])
def explore():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("explore.html", name1=name)
    # starting and empty input default
    url = "https://amazon-product-reviews-keywords.p.rapidapi.com/product/reviews"
    querystring = {"asin":"B07XQXZXJC","country":"US","variants":"1","top":"0"}

    headers = {
    'x-rapidapi-host': "amazon-product-reviews-keywords.p.rapidapi.com",
    'x-rapidapi-key': "f74ed87200msh995f07c2f92be0bp101c14jsn28a6b622e01b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("/explore.html", stats=response.json())


@app.route('/cart/', methods=['GET', 'POST'])
def cart():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("cart.html", name1=name)
    # starting and empty input default
    return render_template("cart.html", name1=" ")


@app.route('/account/', methods=['GET', 'POST'])
def account():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("account.html", name1=name)
    # starting and empty input default
    return render_template("account.html", name1=" ")


@app.route('/blog')
def blog():
    return'''
     <html>
    <head>Techfish  Home . . . Explore . . . Cart . . . Account . . . Mini Labs . . . About Us . . . </head>
    <body>
        <h2> Welcome to TechFish, the best place to buy the best waterproof tech gear! </h2>
        <p> We sell waterproof tech gear! </p>
    </body>
    </html>
    '''


@app.route('/rgb/')
def rgb():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('/rgb.html', images=image_data(path))


@app.route('/prishargb/')
def prishargb():
    path = Path(app.root_path) / "static" / "prishaassets"
    return render_template('/prishrgb.html', images=prisha_image_data(path))


@app.route('/arushirgb/')
def arushirgb():
    path = Path(app.root_path) / "static" / "arushiassets"
    return render_template('/arushirgb.html', images=arushi_image_data(path))


@app.route('/vaishavirgb/')
def vaishavirgb():
    path = Path(app.root_path) / "static" / "vaishaviassets"
    return render_template('/vaishavirgb.html', images=vaishavi_image_data(path))


@app.route('/siyargb/')
def siyargb():
    path = Path(app.root_path) / "static" / "siyaassets"
    return render_template('/siyargb.html', images=siya_image_data(path))


@app.route("/colors", methods=['GET', 'POST'])
def colors():
    return render_template("colorcodes.html")


@app.route("/logicgates", methods=['GET', 'POST'])
def logicgates():
    return render_template("logicgates.html")

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("/joke.html", joke=response.json())


@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("/jokes.html", jokes=response.json())


@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """

    return render_template("/covid19.html", stats=response.json())

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)