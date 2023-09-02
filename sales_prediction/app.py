from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    tv_advertising_value = float(request.form["tv_advertising"])
    predicted_sales = model.predict([[tv_advertising_value]])
    print("Predicted Sales:",predicted_sales[0][0])
    return render_template("index.html",result=predicted_sales[0][0])
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    