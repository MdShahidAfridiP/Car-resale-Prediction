from flask import Flask,render_template,url_for,request
import pickle


app=Flask(__name__)
model=pickle.load(open("trained_model.pickle","rb"))

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    year=2020-int(request.values.get('year'))
    kms=int(request.values.get('kms'))
    seats=int(request.values.get('seats'))
    mileage=int(request.values.get('mileage'))
    engine=int(request.values.get('engine'))
    power=int(request.values.get('power'))
    owner=int(request.values.get('owner'))
    transmission=int(request.values.get('transmission'))
    fuel=int(request.values.get('fuel'))
    location=int(request.values.get('location'))
    data=[year,kms,owner,seats,mileage,engine,power,0,0,0,0,0,0,0,0,0,0,0,0,0,transmission]
    if location!=0:
        data[location]=1
    if fuel!=0:
        data[fuel]=1
    data[-1]=transmission
    result=model.predict([data])
    print(data)
    return render_template("index.html",prediction=(result*100000))
if __name__=="__main__":
    app.run(debug=True)