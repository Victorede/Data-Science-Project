from flask import *
import pickle

import pandas as pd

app = Flask(__name__)
model = pickle.load(open('DecisionTreeClassifier_model.pkl', 'rb'))


@app.route('/')
def Home():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Gender = int(request.form['sex'])
        Chest_Pain_type = int(request.form['Chest_Pain_type'])
        resting_blood_pressure = int(request.form['resting_blood_pressure'])
        cholestoral_in_mgdl = int(request.form['cholestoral_in_mg/dl'])
        fasting_blood_sugar__120_mgdl = int(
            request.form['fasting_blood_sugar_>_120_mg/dl'])
        resting_electrocardiographic = int(
            request.form['resting_electrocardiographic'])
        maximum_heart_rate = int(request.form['maximum_heart_rate'])
        Exercise_induced_angina = int(request.form['Exercise_induced_angina'])
        oldpeak = float(request.form['oldpeak'])

        prediction = model.predict([[Age, Gender, Chest_Pain_type, resting_blood_pressure, cholestoral_in_mgdl,
                                   fasting_blood_sugar__120_mgdl, resting_electrocardiographic, maximum_heart_rate, Exercise_induced_angina, oldpeak]])

        pred = prediction[0]
        #out = "Error"
        if pred == 1:

            pred = "Significant risk of developing heart failure"
        else:

            pred = "less chances of developing of heart failure"
        return render_template('index.html', results=pred)

    else:
        return render_template('index.html')

if __name__ == "__main__":
	app.run(debug = True)
