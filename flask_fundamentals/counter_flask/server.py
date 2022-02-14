from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'oooo its a secret'
app.count = 0

@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html', count=session['count'])

@app.route('/clear', methods=['POST'])
def clear_counter():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)