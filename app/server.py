import re
from flask import Flask, render_template, request

app = Flask(__name__)

member_repo = [
    {'id': "2015112537", 'pw': "1234"},
    {'id': "2019113173", 'pw': "1234"},
    {'id': "2016111952", 'pw': "1234"}
]

user_info = dict()

@app.route('/')
def student():
   return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        user_info['id'] = request.form.get('id')
        user_info['pw'] = request.form.get('pw')

        for info in member_repo:
            if info['id'] == user_info['id'] and info['pw'] == user_info['pw']:
                return render_template("application_form.html", user_info=user_info)
        
        error = "login fail"
        return render_template("login.html", error=error)



@app.route('/submit', methods=['GET', 'POST'])
def result():
    forms = dict()
    if request.method == 'POST':
        forms['name'] = request.form.get('uname')
        forms['major'] = request.form.get('umajor')
        forms['id'] = request.form.get('uid')
        forms['score'] = request.form.get('score')
        forms['opinion'] = request.form.get('opinion')

        return render_template("submit.html", forms=forms)


if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
