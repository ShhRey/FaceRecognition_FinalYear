from flask import Flask, render_template, url_for
app = Flask(__name__)

import sum

@app.route('/')
def home():
    return render_template('login.html')




@app.route('/traintest')
def traintest():
    import createData
    return sum.traintest()

@app.route("/bcd")
def bcd():
    return sum.bcd()

if __name__ == '__main__':
    app.run(debug=True)