from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('savemodel.sav','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict',methods =['POST','GET'])
def predict():
    HighBP = float(request.form['HighBP'])
    HighChol = float(request.form['HighChol'])
    CholCheck = float(request.form['CholCheck'])
    BMI = float(request.form['BMI'])
    Smoker = float(request.form['Smoker'])
    Stroke = float(request.form['Stroke'])
    HeartDiseaseorAttack = float(request.form['HeartDiseaseorAttack'])
    PhysActivity = float(request.form['PhysActivity'])
    FruitsVeggies = float(request.form['Fruits Veggies'])
    HvyAlcoholConsump = float(request.form['HvyAlcoholConsump'])
    AnyHealthcare = float(request.form['AnyHealthcare'])
    NoDocbcCost = float(request.form['NoDocbcCost'])
    GenHlth = float(request.form['GenHlth'])
    MentHlth = float(request.form['MentHlth'])
    PhysHlth = float(request.form['PhysHlth'])
    DiffWalk = float(request.form['DiffWalk'])
    Sex = float(request.form['Sex'])
    Age = float(request.form['Age'])
    Education = float(request.form['Education'])
    Income = float(request.form['Income'])
    result = model.predict([HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,HeartDiseaseorAttack,PhysActivity,FruitsVeggies,HvyAlcoholConsump,AnyHealthcare,NoDocbcCost,GenHlth,MentHlth,PhysHlth,DiffWalk, Sex, Age, Education,Income])[0]
    return render_template('index.html',**locals())

if __name__ == '__main__':
    app.run(debug = True)