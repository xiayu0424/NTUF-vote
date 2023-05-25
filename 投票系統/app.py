from verified import verified
import flask
from flask import render_template,jsonify,request
from crypt import rc4_algorithm
import os
import pathlib
import json
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

SRC_PATH =  pathlib.Path(__file__).parent.absolute()
UPLOAD_FOLDER = os.path.join(SRC_PATH, 'uploads')


app = flask.Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')



@app.route("/verify.html")
def verify():
    return render_template("verify.html", value='0')



@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        if request.values['send'] == '送出':
            id = request.values.get("id")
            name = request.values.get("name")
            # img = request.files['img']
            key = rc4_algorithm("encrypt",id)
        # if img.filename != '':
        #     path=str(id)+img.filename[-4:]
        #     img.save(os.path.join(UPLOAD_FOLDER, path))
        #     img_path = os.path.join(UPLOAD_FOLDER, path)            

            if(verified(id,name,key)) :        
                return render_template('verify.html',passw=key,value='1')
            else:
                return render_template('verify.html',value='2') 
    else:
        return render_template('verify.html',value='2') 

@app.route("/vote.html")
def vote():
    return render_template("vote.html",voted='0')

@app.route("/vote", methods=['GET', 'POST'])
def voting():
    if request.method == 'POST':
        if request.values['send'] == '確認投票':
            with open("data.json", 'r') as f:
                    data = json.load(f)
            result = request.values.get('people')
            password = request.values.get('pass')
            if(password in data["password"]):
                return render_template('vote.html',voted='2')
            else:
                data['password'].append(password)
                if(result=="1"):
                    data["vote"]["Agree"] +=1
                    with open('data.json','w',encoding='utF8') as f:
                        json.dump(data,f,indent=4)
                elif(result=="2"):
                    data["vote"]["Disagree"] +=1
                    with open('data.json','w',encoding='utF8') as f:
                        json.dump(data,f,indent=4)
                
                return render_template('vote.html',voted='1')

@app.route('/background')
def back():
    with open("data.json", 'r') as f:
        data = json.load(f)
    return render_template('back.html',voted=list(data['vote'].values()),name=list(data['data'].keys()),num=["No.1","No.2"])

    
    

if __name__ == '__main__':
    #app.run()
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    print("success")
    http_server.serve_forever()