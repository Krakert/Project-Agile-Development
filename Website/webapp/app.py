from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


# routes aangemaakt zodat er genavigeerd kan worden!
@app.route('/')
@app.route('/home')
@app.route('/Home')
@app.route('/index')
@app.route('/Index')
def main():
    return render_template('index.html', title='PAD Team 7 NAO')

@app.route('/sudoku')
def sudoku():
    return render_template('minigames_sudoku.html', title='Maak een sudoku')

@app.route('/Rekenen')
@app.route('/rekenen')
def Rekenen():
    return render_template('minigames_rekenen.html', title='Kies een niveau')

@app.route('/rekenen/niveau1')
def RekenenN1():
    return render_template('minigames_rekenen_n1.html', title='Rekenen niveau 1')

@app.route('/rekenen/niveau2')
def RekenenN2():
    return render_template('minigames_rekenen_n2.html', title='Rekenen niveau 2')

@app.route('/rekenen/niveau3')
def RekenenN3():
    return render_template('minigames_rekenen_n3.html', title='Rekenen niveau 3')

@app.route('/Minigames')
@app.route('/minigames')
def minigames():
    return render_template('minigames.html', title='Blijft bezig')


@app.route('/Beweeg')
@app.route('/beweeg')
def beweeg():
    return render_template('beweeg.html', title='Lekker in beweeging')


@app.route('/Ondersteuning')
@app.route('/ondersteuning')
def ondersteuning():
    return render_template('ondersteuning.html', title='Vraag naar hulp')

# @app.route('/Bestel')
# @app.route('/bestel')
# def bestel():
#     return render_template('bestel.html', title='Bestel')

@app.route('/Nieuws')
@app.route('/nieuws')
def nieuws():
    return render_template('nieuws.html', title='Blijf op de hoogte')

@app.route('/Muziek')
@app.route('/muziek')
def muziek():
    return render_template('muziek.html', title='Speel een lied')

# debug = True, keeps the server alive
if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True)
