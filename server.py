# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("templates/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    requested_year = request.args.get('year')
    print(requested_year)
    if requested_year == None:
        requested_year = "1960"
    return render_template('index.html', data = data, year = requested_year)

@app.route('/year')
def year():
    f = open("templates/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    requested_year = request.args.get('year')
    return render_template('year.html', data = data, year = requested_year)

app.run(debug=True)
