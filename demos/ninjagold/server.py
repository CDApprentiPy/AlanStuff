from flask import Flask, render_template, session, request, redirect
from Message import Message

app = Flask(__name__)
app.secret_key = "thegoodgood"

# basic route that loads page and displays information
@app.route('/')
def main():
    # total gold?
    if 'muns' not in session:
        session['muns'] = 0
    # messages?
    if 'mess' not in session:
        session['mess'] = []
        session['mess'].append('You started NInja Gold')
    context = {
        'money': session['muns'],
        'mess': session['mess'],
    }
    return render_template("index.html", context=context)

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

# route that handles moneys
@app.route("/process", methods=['POST'])
def process():
    # farm, mine, gamble, dragon
    print('Processing stuff')
    activity = request.form['activity']
    print(activity)
    if activity == 'farm':
        # add 10-20 golds to muns
        session['muns'] = session['muns'] + 14
    elif activity == 'mine':
        # do other stuff 
        session['muns'] = session['muns'] + 14
    elif activity == 'gamble':
        # do some stuff 
        session['muns'] = session['muns'] + 14
    else:
        # do some other stuff
        session['muns'] = session['muns'] + 14
    session['mess'].append(Message(activity, 14).to_message())
    return redirect('/')
    

app.run(debug=True)