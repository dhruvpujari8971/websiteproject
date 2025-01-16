from flask import Flask
from flask import render_template
import datetime
import requests


response=requests.get(url=f"https://api.agify.io?name=")
response.raise_for_status()

app=Flask(__name__)

@app.route('/')
def home():
    years=datetime.datetime.now().year
    return render_template('index.html',year=years)

@app.route('/guess/<name>')
def guess(name):
    response=requests.get(url=f"https://api.agify.io?name={name}")
    # response.raise_for_status()
    data=response.json()
    data_file=data["age"]
    gender_url=requests.get(f"https://api.genderize.io?name={name}")
    gender=gender_url.json()
    gender_data=gender["gender"]
    ask=requests.get(" https://api.npoint.io/41ac2da683d0ab43062a") 
    get=ask.json()
    data_get=get["why"]
    return render_template('guess.html',ages=data_file,name=name,gender=gender_data,know=get)

@app.route('/blog')
def blog():
    response=requests.get(" https://api.npoint.io/44fb98e6e76ef1131c2b")
    data=response.json()
    data_s=data["hiee"]
    return render_template('blog.html',datas=data_s)

@app.route('/Webporject')
def web():
    response=requests.get("http://127.0.0.1:3000/11.2 Bootstrap Components/index.html")
    return render_template('web.html')





if __name__=="__main__":
   app.run(debug=True)



