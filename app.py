from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    values = [float(x) for x in request.form.values()]
    input_data = np.array([values])
    prediction = model.predict(input_data)
    
    result = "Fraud" if prediction[0] == 1 else "Not Fraud"
    return render_template('index.html', prediction_text=f'Transaction is: {result}')

if __name__ == "__main__":
    app.run(debug=True)


