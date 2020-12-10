from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random, requests, asyncio, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login/login.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    password = request.form['password']
    email = request.form['email']
    
    authpassword = "qwerty"
    authemail = "qwerty@admin.com"

    if password == authpassword and email == authemail:
        return ("login successful")
    else: 
        return ("Access Denied")

    return render_template('login/login.html')

@app.route('/cointoss')
def cointoss():
    
    outcomes = ['Heads!', 'Tails!']
    result = random.choice(outcomes)

    return render_template('cointoss/cointoss.html', result=result)

@app.route('/rps', methods=['GET', 'POST'])
def play():
    if request.method=='POST':
        return render_template('RPS/rps.html', choice=rps())
    else:
        return render_template('RPS/rps.html')

def rps():
    return random.randint(1, 3)

@app.route('/eightball')
def eightball():
    return render_template('8ball/8ball.html')

@app.route('/8ball', methods=['POST'])
def magic8ball():

    possibleresponses = [
            "Yes.",
            "Sure, why not?",
            "Without a doubt",
            "You may rely on it.",
            "Yeah, probably.",
            "I don't feel like answering right now. Try again later.",
            "Cannot predict now.",
            "It is illegal for me to answer.",
            "Nope!",
            "My reply is no.",
            "Very doubtful."
        ]
    answer = random.choice(possibleresponses)
    
    question = request.form['question']

    return render_template('8ball/answer.html', answer=answer, question=question)

@app.route('/teams')
def teams():

    people = ['Jim', 'Jimmy', 'Jimmy Jr', 'Jimmy Jr Jr', 'Jimmy Sr', 'Jimmy Sr Jr', 'Jimmy Jr Jr Jr', 'Sir Jimmy III', 'Jimmy IV', 'Jimmy V', 'Jimmy VI', 'Jimmy VII', 'Lenny']
    t1, t2 = [], []
    for x in range(len(people)):
        person = random.choice(people)
        people.remove(person)
        if x % 2 == 0:
            t1.append(person)
        else:
            t2.append(person)

    return render_template("teams/students.html", t1=t1, t2=t2)

@app.route('/game')
def madlibsgame():
    return render_template("madlibs/game.html")

@app.route('/madlibs', methods=['POST'])
def madlibs():


    name = request.form['name']
    relative = request.form['relative']
    colour = request.form['colour']
    adjective = request.form['adjective']
    mood = request.form['mood']
    item = request.form['item']


    return render_template("madlibs/madlibs.html", name=name, relative=relative, colour=colour, adjective=adjective, mood=mood, item=item)

@app.route('/gstcalc', methods=['GET', 'POST'])
def gstcalc():
    if request.method == "POST":
            
        gst = float(request.form['gst'].replace('$', ''))
        gst/=11
        gst = round(gst, 2)
        return str(gst)
    else:
        return render_template('GST/gst.html')

@app.route('/chucknorris')
def chuck():

    return render_template('chucknorris/chucknorris.html')

@app.route('/chucknorris/random')
def chucknorris():
    url = 'https://api.chucknorris.io/jokes/random'
    jokeJSON = requests.get(url).json()['value']

    return jokeJSON

@app.route('/chucknorris/categories')
def categories():
    url = 'https://api.chucknorris.io/jokes/categories'
    categories = requests.get(url).json()

    return render_template('chucknorris/joke.html', categories=categories)

@app.route('/chucknorris/categories/<category>')
def cat(category):
    url = 'https://api.chucknorris.io/jokes/random?categroy=' + category
    jokeJSON = requests.get(url).json()['value']

    return render_template('chucknorris/joke.html', jokeJSON=jokeJSON)

@app.route('/advice')
def advice():
    url = 'https://api.adviceslip.com/advice'
    r = requests.get(url).json()

    advice = {
        'advice' : r['slip']['advice']
    }

    return render_template('advice/advice.html', advice=advice)

@app.route('/dadjoke')
def dadjoke():
    url = 'https://icanhazdadjoke.com/'
    joke = requests.get(url, headers={"Accept":'application/json '}).json()

    return render_template('dadjoke/dadjoke.html', joke=joke['joke'])


@app.route('/weather')
def weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0f2562c400ea2d1ac2a89f53eff95cd0'
    city = 'Montreal'

    r = requests.get(url.format(city)).json()

    weather = {
        'city' : city,
        'temperature' : r['main']['temp'] ,
        'description' : r['weather'][0]['description'] ,
        'icon' : r['weather'][0]['icon'] ,
    }

    return render_template('weather/weather.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)