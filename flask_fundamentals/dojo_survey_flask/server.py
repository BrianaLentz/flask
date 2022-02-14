from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'wow so secretive'

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['loc'] = request.form['location']
    session['lang'] = request.form['language']
    session['comm'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name_on_template=session['name'], location_on_template=session['loc'], language_on_template=session['lang'], comments_on_template=session['comm'])
    

if __name__=="__main__":
    app.run(debug=True)