from flask import Flask, render_template, redirect, request, session
from random import randint, randrange
from datetime import datetime

app = Flask(__name__)
app.secret_key = "mysupersecretkey"


@app.route("/")
def index():
    print('from index')
    if not 'random_number' in session:
        session['random_number'] = 0
        session['activities'] = []

    print(session['random_number'])
    print('*'*40)
    return render_template("index.html")

@app.route("/process_money/<building>", methods=['POST'])
def process(building):
    print(request.form)
    # when using route parameters
    print(building)
    gold = {
        'farm': randint(10, 20),
        'cave': randint(5, 10),
        'house': randint(2, 5),
        'casino': randint(-50, 50)
    }
    # if request.form['building'] == 'farm':
    #     ran_num = randint(10, 20)

    # if request.form['building'] == 'cave':
    #     ran_num = randint(5, 10)

    # if request.form['building'] == 'house':
    #     ran_num = randint(2, 5)

    # if request.form['building'] == 'casino':
    #     ran_num = randint(-50, 50)

    session['random_number'] += gold[building]
    date_time = datetime.now()
    # https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.date.month
    print(date_time.day)
    print(date_time.year)
    print(date_time.month)
    # https://stackabuse.com/how-to-format-dates-in-python/
    print(date_time.strftime("%b %d %Y %H:%M:%S"))
    time_stamp = date_time.strftime("%b %d %Y %H:%M:%S")

    # build the activity log
    # if ran_num > 0:
    if gold[request.form['building']] > 0:
        # using lookup dictonary instead of conditionals
        session['activities'].append(f"<p class='text-success'>You entered a {request.form['building']} and gained {gold[request.form['building']]} gold pieces! @ {time_stamp}</p>")
        # using 
        # session['activities'].append(f"<p class='text-success'>You entered a {request.form['building']} and gained {ran_num} gold pieces! @ {time_stamp}</p>")
    else:
        # using lookup dictonary instead of conditionals
        session['activities'].append(f"<p class='text-danger'>You entered a {request.form['building']} and lost {abs(gold[request.form['building']])} gold pieces! @ {time_stamp}</p>")
        # session['activities'].append(f"<p class='text-danger'>You entered a {request.form['building']} and lost {abs(ran_num)} gold pieces! @ {time_stamp}</p>")
    print('from process')
    # print(ran_num)
    print(datetime.now())
    print('*'*40)

    return redirect("/")

@app.route('/play_again')
def play_again():
    print('-'*50)
    print(request.form)
    print(request.url)
    print('-'*50)
    session.clear()
    return redirect("/")


app.run(debug=True)