from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/send', methods = ['GET','POST'])
def send():
    if request.method =="post":
        text=request.form['text']
        return render_template("main.html",text=text)
    return render_template('index.html')