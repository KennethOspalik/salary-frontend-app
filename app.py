from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_url = "https://YOUR-AZURE-API-NAME.azurewebsites.net/predict"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict():
    user_input = {
        "age": request.form.get("age"),
        "education": request.form.get("education"),
        "job_title": request.form.get("job_title"),
        "years_experience": request.form.get("years_experience"),
        "state": request.form.get("state")
    }

    response = requests.post(api_url, json=user_input)

    if response.status_code == 200:
        result = response.json().get("predicted_salary", "Prediction error")
    else:
        result = "API error"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
