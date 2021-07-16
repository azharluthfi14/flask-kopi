from flask import Blueprint, render_template, request
import joblib
import numpy as np
# from .models import db, CoffeeQuality

coffee = Blueprint('coffee', __name__)


@coffee.route('/')
def landing():
    return render_template('page/index.html')


@coffee.route('/classification')
def classification():
    return render_template('page/classification.html')


@coffee.route('/classification', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        aroma = request.form['aroma']
        flavor = request.form['flavor']
        aftertaste = request.form['aftertaste']
        acidity = request.form['acidity']
        body = request.form['body']
        balance = request.form['balance']

        test_data = [aroma, flavor, aftertaste, acidity, body, balance]
        clean_data = [float(arr_data) for arr_data in test_data]
        matrix = np.array(clean_data).reshape(1, -1)

        model = joblib.load(
            'F:/Flask-Project/flask-kopi/core/core/coffee/model/model_kopi_NB.pkl')

        quality = model.predict(matrix)
        result_quality = quality[0]
        if result_quality == [0]:
            coffe_class = "Fair quality"
        elif result_quality == [1]:
            coffe_class = "Good quality"
        elif result_quality == [2]:
            coffe_class = "Excellent quality"

        return render_template('page/classification.html', coffe_class=coffe_class, aroma=aroma, flavor=flavor, aftertaste=aftertaste, acidity=acidity, body=body, balance=balance)
