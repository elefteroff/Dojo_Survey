from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "It's a secret"

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def returned_form():
    if request.method == 'POST':
        session['namefield'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def info():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)