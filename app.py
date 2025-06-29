from flask import Flask, render_template, ruquests
form sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

#predicting using model saved using pickle
model = pickle.load(open("iris_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        swidth = float(request.form.get("swidth"))
        sheight = float(request.form.get("sheight"))
        pwidth = float(request.form.get("pwidth"))
        pheight = float(request.form.get("pheight"))
        prediction = model.predict([[swidth, sheight, pwidth, pheight]])
        return render_template("index.html", data=prediction[0])
    except Exception as e:
        return render_template("index.html", data=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run()
