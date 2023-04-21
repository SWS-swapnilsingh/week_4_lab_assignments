from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def funct():
    if request.method =='GET':
        return render_template('form.html')
    if request.method =='POST':
        name = request.form.get('info')
        course = request.form.get('course')
        pro = request.form.get('prof')
        gender = request.form.get('gender')
        quote = request.form.get('quote')
        data = [name, course, pro, gender, quote]
        return render_template('output.html',data=data)


# @app.route('/output', methods = ['GET','POST'])
# def funct():
app.run(debug=True)

