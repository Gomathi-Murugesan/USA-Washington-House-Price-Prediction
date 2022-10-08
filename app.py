from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

## this route function is used to get cities name in the drop down of ui
## the function to get cities name is in util.py file

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_cities_name')
def get_cities_name():
    response = jsonify({
        'cities': util.get_cities_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    sqft_living = float(request.form['sqft_living'])
    city = request.form['city']
    bathrooms = request.form['bathrooms']
    bedrooms = request.form['bedrooms']
    yr_built = request.form['yr_built']

    response = jsonify({
        'estimated_price': util.get_estimated_house_price(city, sqft_living, bathrooms, bedrooms, yr_built)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print('Starting our server')
    util.load_artifacts()
    app.run()
