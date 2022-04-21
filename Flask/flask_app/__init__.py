from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/')
def result():
    age = int(request.args.get("age"))
    gender = int(request.args.get("gender"))
    height = int(request.args.get("height"))
    weight = float(request.args.get("weight"))
    ap_hi = int(request.args.get("ap_hi"))
    ap_lo = int(request.args.get("ap_lo"))
    cholesterol = int(request.args.get("cholesterol"))
    gluc = int(request.args.get("gluc"))
    smoke = int(request.args.get("smoke"))
    alco = int(request.args.get("alco"))
    active = int(request.args.get("active"))

    import pickle
    

    model = None
    with open('../../DataModel/model.pkl','rb') as pickle_model:
        model = pickle.load(pickle_model)

    data = [[age*365,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active]]
    prob = model.predict_proba(data)[0][1]*100
    

    return render_template('result.html',Age=age,Gender=gender,Height=height,Weight=weight,Sbp=ap_hi,Dbp=ap_lo,Cholesterol=cholesterol,Glucose=gluc,Smoking=smoke,Alcohol=alco,
                            Pa=active,prob=prob)


if __name__ == '__main__':
    app.run(debug=True)