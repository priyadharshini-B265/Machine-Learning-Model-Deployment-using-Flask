import pickle
from flask import Flask,render_template,request








#class,Objects,Methods,Inheritance,Polymorphism,Abstraction,Enacapsulation
#Decoration,Generastors,Dunder Methods,Abstract methods,static methods


#create and object of the class Flask

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb')) # to unpickle to load the model



@app.route('/')   # endpoint of url ,by default takes GET method
def index():
    return render_template('index.html') #return HTML page


@app.route('/predict',methods = ['GET','POST'])

def predict():
    temp = request.form.get('temperature')
    prediction = model.predict([[temp]])
    output = round(prediction[0],2) #prediction[0] is 1st index ,round 2 decimal
    print(output)
    return render_template('result.html',prediction_test=f' For the Temperature {temp} C ,The Total Revenue generated is Rs.{output}/-') #to display output


if __name__=='__main__':   # to run the app 
    app.run(debug=True)    #error will automatically flask on terminal